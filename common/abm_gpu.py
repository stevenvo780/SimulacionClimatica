"""
abm_gpu.py — Motor ABM GPU con CuPy para calibración masiva paralela.

La idea clave: en vez de ejecutar 5135 simulaciones secuencialmente,
ejecutar BATCH_SIZE simulaciones EN PARALELO en la GPU.
Cada simulación tiene su propia grilla, pero comparten el mismo forcing.
Los parámetros (fs, mc, dmp) varían por batch.

Grid shape: (batch, n, n) — cada batch es una simulación independiente.
Con batch=512 y n=20: 512×20×20 = 204800 celdas → GPU domina.
"""

import numpy as np

try:
    import cupy as cp
    GPU_AVAILABLE = True
except ImportError:
    GPU_AVAILABLE = False


def _neighbor_mean_batch(grid, xp):
    """Promedio de vecinos para batch de grids: (B, N, N)."""
    # Padded approach for non-periodic boundaries
    B, N, _ = grid.shape
    acc = xp.zeros_like(grid)
    count = xp.full_like(grid, 0.0)

    # Up
    acc[:, 1:, :] += grid[:, :-1, :]
    count[:, 1:, :] += 1
    # Down
    acc[:, :-1, :] += grid[:, 1:, :]
    count[:, :-1, :] += 1
    # Left
    acc[:, :, 1:] += grid[:, :, :-1]
    count[:, :, 1:] += 1
    # Right
    acc[:, :, :-1] += grid[:, :, 1:]
    count[:, :, :-1] += 1

    return acc / count


def batch_simulate_abm(param_sets, forcing, steps, n, init_center=0.0,
                       init_range=0.5, seed=2, device_id=0):
    """
    Simula BATCH_SIZE ABMs en paralelo en la GPU.

    Args:
        param_sets: list of (forcing_scale, macro_coupling, damping)
        forcing: list of float, forcing series (shared)
        steps: int
        n: grid_size
        init_center: center for grid init
        init_range: range for uniform init
        seed: random seed
        device_id: GPU device id

    Returns:
        macro_series: np.ndarray (batch, steps) — series temporal de cada sim
    """
    if GPU_AVAILABLE:
        try:
            return _batch_simulate_gpu(param_sets, forcing, steps, n,
                                       init_center, init_range, seed, device_id)
        except Exception:
            pass
    return _batch_simulate_cpu(param_sets, forcing, steps, n,
                               init_center, init_range, seed)


def _batch_simulate_gpu(param_sets, forcing, steps, n, init_center,
                        init_range, seed, device_id):
    """GPU implementation using CuPy."""
    cp.cuda.Device(device_id).use()
    xp = cp
    B = len(param_sets)

    rng = np.random.RandomState(seed)
    grid_np = init_center + rng.uniform(-init_range, init_range, (B, n, n)).astype(np.float32)
    grid = xp.asarray(grid_np)

    # Pre-generate all noise on CPU, transfer to GPU
    noise_np = rng.uniform(-0.01, 0.01, (steps, B, n, n)).astype(np.float32)
    noise_gpu = xp.asarray(noise_np)

    # Parameters as GPU arrays: (B, 1, 1) for broadcasting
    fs_arr = xp.array([p[0] for p in param_sets], dtype=xp.float32).reshape(B, 1, 1)
    mc_arr = xp.array([p[1] for p in param_sets], dtype=xp.float32).reshape(B, 1, 1)
    dmp_arr = xp.array([p[2] for p in param_sets], dtype=xp.float32).reshape(B, 1, 1)

    forcing_arr = xp.asarray(forcing[:steps], dtype=xp.float32)
    macro_series = xp.zeros((B, steps), dtype=xp.float32)

    for t in range(steps):
        f = forcing_arr[t]
        macro = grid.mean(axis=(1, 2)).reshape(B, 1, 1)  # (B, 1, 1)

        nb_mean = _neighbor_mean_batch(grid, xp)

        grid = (
            grid
            + 0.2 * (nb_mean - grid)  # diffusion fixed at 0.2
            + fs_arr * f
            + mc_arr * (macro - grid)
            - dmp_arr * grid
            + noise_gpu[t]
        )
        # Clamp
        xp.clip(grid, -50.0, 50.0, out=grid)

        macro_series[:, t] = grid.mean(axis=(1, 2))

    return cp.asnumpy(macro_series)


def _batch_simulate_cpu(param_sets, forcing, steps, n, init_center,
                        init_range, seed):
    """CPU fallback using NumPy."""
    xp = np
    B = len(param_sets)

    rng = np.random.RandomState(seed)
    grid = init_center + rng.uniform(-init_range, init_range, (B, n, n)).astype(np.float32)

    noise = rng.uniform(-0.01, 0.01, (steps, B, n, n)).astype(np.float32)

    fs_arr = np.array([p[0] for p in param_sets], dtype=np.float32).reshape(B, 1, 1)
    mc_arr = np.array([p[1] for p in param_sets], dtype=np.float32).reshape(B, 1, 1)
    dmp_arr = np.array([p[2] for p in param_sets], dtype=np.float32).reshape(B, 1, 1)

    macro_series = np.zeros((B, steps), dtype=np.float32)

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        macro = grid.mean(axis=(1, 2)).reshape(B, 1, 1)

        nb_mean = _neighbor_mean_batch(grid, xp)

        grid = (
            grid
            + 0.2 * (nb_mean - grid)
            + fs_arr * f
            + mc_arr * (macro - grid)
            - dmp_arr * grid
            + noise[t]
        )
        np.clip(grid, -50.0, 50.0, out=grid)
        macro_series[:, t] = grid.mean(axis=(1, 2))

    return macro_series


def gpu_calibrate(obs_train, forcing_series, steps, n, init_center=0.0,
                  init_range=0.5, seed=2, param_grid=None, n_refine=2000,
                  batch_size=512, device_id=0):
    """
    Calibración masiva usando GPU batch.
    
    En vez de 5135 evals secuenciales (~30min), hace:
    - 3135 combos en ~7 batches de 512 (~1min en GPU)
    - 2000 refine en ~4 batches de 512 (~30s en GPU)
    Total: ~2min vs 30min = 15x speedup
    """
    if param_grid is None:
        param_grid = {
            "forcing_scale": [0.001, 0.005, 0.01, 0.02, 0.04, 0.06, 0.08, 0.12,
                              0.18, 0.25, 0.35, 0.45, 0.55, 0.65, 0.8, 0.95,
                              1.1, 1.3, 1.5],
            "macro_coupling": [0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7,
                               0.8, 0.9, 0.95],
            "damping": [0.0, 0.005, 0.01, 0.03, 0.06, 0.1, 0.15, 0.2,
                        0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
        }

    # Generate all combos
    combos = []
    for fs in param_grid["forcing_scale"]:
        for mc in param_grid["macro_coupling"]:
            for dmp in param_grid["damping"]:
                combos.append((fs, mc, dmp))

    obs_arr = np.asarray(obs_train, dtype=np.float32)
    n_obs = len(obs_train)

    # Process in batches
    all_errors = []
    for i in range(0, len(combos), batch_size):
        batch = combos[i:i + batch_size]
        series = batch_simulate_abm(batch, forcing_series, steps, n,
                                     init_center, init_range, seed, device_id)
        # Compute RMSE for each
        for j, (fs, mc, dmp) in enumerate(batch):
            pred = series[j, :n_obs]
            err = float(np.sqrt(np.mean((pred - obs_arr) ** 2)))
            all_errors.append((err, fs, mc, dmp))

    all_errors.sort(key=lambda x: x[0])
    best = all_errors[0]
    best_params = {"forcing_scale": best[1], "macro_coupling": best[2], "damping": best[3]}
    best_err = best[0]

    # Refinement in batches
    import random as rnd
    rng = rnd.Random(seed + 100)
    refine_combos = []
    for _ in range(n_refine):
        refine_combos.append((
            max(0.001, min(1.5, best_params["forcing_scale"] + rng.uniform(-0.05, 0.05))),
            max(0.1, min(1.0, best_params["macro_coupling"] + rng.uniform(-0.1, 0.1))),
            max(0.0, min(0.9, best_params["damping"] + rng.uniform(-0.05, 0.05))),
        ))

    for i in range(0, len(refine_combos), batch_size):
        batch = refine_combos[i:i + batch_size]
        series = batch_simulate_abm(batch, forcing_series, steps, n,
                                     init_center, init_range, seed, device_id)
        for j, (fs, mc, dmp) in enumerate(batch):
            pred = series[j, :n_obs]
            err = float(np.sqrt(np.mean((pred - obs_arr) ** 2)))
            if err < best_err:
                best_params = {"forcing_scale": fs, "macro_coupling": mc, "damping": dmp}
                best_err = err

    return best_params, best_err, all_errors[:5]
