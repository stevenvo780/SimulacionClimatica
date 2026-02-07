"""
abm_numpy.py — Motor ABM vectorizado con NumPy.

Reemplaza los loops Python puro por operaciones vectorizadas.
Speedup esperado: 50-100x sobre la implementación de listas.

La dinámica es idéntica a los ABMs individuales:
  new_grid = grid
    + diff * (neighbor_mean - grid)
    + forcing_scale * f
    + macro_coupling * (macro - grid)
    - damping * grid
    + noise

La difusión usa convolución con kernel de vecinos (roll + promedio).
"""

import numpy as np


def _neighbor_mean(grid):
    """Promedio de vecinos 4-conectados usando np.roll (borde periódico corregido)."""
    n = grid.shape[0]
    acc = np.zeros_like(grid)
    count = np.full_like(grid, 4.0)

    acc += np.roll(grid, 1, axis=0)   # arriba
    acc += np.roll(grid, -1, axis=0)  # abajo
    acc += np.roll(grid, 1, axis=1)   # izquierda
    acc += np.roll(grid, -1, axis=1)  # derecha

    # Corregir bordes (no son periódicos en el ABM original)
    # Fila 0: no tiene vecino arriba
    acc[0, :] -= np.roll(grid, 1, axis=0)[0, :]
    count[0, :] -= 1
    # Fila n-1: no tiene vecino abajo
    acc[-1, :] -= np.roll(grid, -1, axis=0)[-1, :]
    count[-1, :] -= 1
    # Col 0: no tiene vecino izquierda
    acc[:, 0] -= np.roll(grid, 1, axis=1)[:, 0]
    count[:, 0] -= 1
    # Col n-1: no tiene vecino derecha
    acc[:, -1] -= np.roll(grid, -1, axis=1)[:, -1]
    count[:, -1] -= 1

    return acc / count


def simulate_abm_numpy(params, steps, seed=2, series_key="tbar",
                       init_center=0.0, init_range=0.5,
                       store_grid=True):
    """
    ABM vectorizado. Compatible con la interfaz de todos los casos.

    Args:
        params: dict con grid_size, diffusion, noise, macro_coupling,
                forcing_scale, damping, forcing_series, etc.
        steps: número de pasos
        seed: semilla para reproducibilidad
        series_key: nombre de la serie principal en el resultado
        init_center: centro de inicialización (default 0.0, clima usa t0)
        init_range: rango de inicialización uniforme
        store_grid: si True, almacena grid completo (necesario para métricas)

    Returns:
        dict con series_key, "grid", "forcing"
    """
    rng = np.random.RandomState(seed)
    n = params.get("grid_size", 20)
    diff = params.get("diffusion", 0.2)
    noise_amp = params.get("noise", 0.02)
    mc = params.get("macro_coupling", 0.3)
    fs = params.get("forcing_scale", 0.01)
    dmp = params.get("damping", 0.02)
    assim_series = params.get("assimilation_series")
    assim_strength = params.get("assimilation_strength", 0.0)

    # Inicialización
    center = params.get("t0", init_center)
    grid = center + rng.uniform(-init_range, init_range, (n, n))

    forcing = params.get("forcing_series")
    if forcing is None:
        # Generar forcing sinusoidal (caso_clima style)
        base = params.get("forcing_base", 0.0)
        trend = params.get("forcing_trend", 0.0)
        amp = params.get("forcing_seasonal_amp", 0.0)
        period = params.get("forcing_seasonal_period", 12.0)
        t_arr = np.arange(steps)
        forcing = base + trend * t_arr + amp * np.sin(2 * np.pi * t_arr / period)
        forcing = forcing.tolist()

    main_series = []
    grid_series = [] if store_grid else None

    for t in range(steps):
        f = forcing[t]
        macro = grid.mean()

        # Difusión vectorizada
        nb_mean = _neighbor_mean(grid)

        # Update vectorizado completo
        noise_matrix = rng.uniform(-noise_amp, noise_amp, (n, n))
        grid = (
            grid
            + diff * (nb_mean - grid)
            + fs * f
            + mc * (macro - grid)
            - dmp * grid
            + noise_matrix
        )

        # Nudging
        if assim_series is not None and t < len(assim_series):
            target = assim_series[t]
            if target is not None:
                macro_post = grid.mean()
                grid += assim_strength * (target - macro_post)

        macro_final = float(grid.mean())
        main_series.append(macro_final)

        if store_grid:
            grid_series.append(grid.tolist())

    result = {
        series_key: main_series,
        "forcing": forcing if isinstance(forcing, list) else forcing.tolist(),
    }
    if store_grid:
        result["grid"] = grid_series
    return result


def make_abm_adapter(series_key, init_center=0.0, init_range=0.5):
    """
    Crea un adaptador compatible con la interfaz simulate_abm(params, steps, seed).

    Usage en validate.py:
        from common.abm_numpy import make_abm_adapter
        simulate_abm = make_abm_adapter("tbar", init_center=14.0, init_range=0.5)
    """
    def simulate_abm(params, steps, seed=2):
        # En calibración no necesitamos grid (ahorra ~80% de memoria)
        store = params.get("_store_grid", True)
        return simulate_abm_numpy(
            params, steps, seed=seed,
            series_key=series_key,
            init_center=params.get("t0", init_center),
            init_range=init_range,
            store_grid=store,
        )
    return simulate_abm
