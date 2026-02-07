import numpy as np
import random


def simulate_abm(params, steps, seed):
    random.seed(seed)
    n = params["grid_size"]
    diff = params["diffusion"]
    noise = params["noise"]
    macro_coupling = params["macro_coupling"]
    forcing_scale = params.get("forcing_scale", 0.01)
    damping = params.get("damping", 0.02)
    attention_scale = params.get("attention_scale", 0.05)
    assimilation_series = params.get("assimilation_series")
    assimilation_strength = params.get("assimilation_strength", 0.0)
    _store_grid = params.get("_store_grid", True)

    grid = [[params["a0"] + random.uniform(-0.2, 0.2) for _ in range(n)] for _ in range(n)]

    forcing = params["forcing_series"]
    w = params["w0"]
    w_series = []
    grid_series = [] if _store_grid else None

    for t in range(steps):
        f = forcing[t]

        new_grid = [[0.0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                neighbors = []
                if i > 0:
                    neighbors.append(grid[i - 1][j])
                if i < n - 1:
                    neighbors.append(grid[i + 1][j])
                if j > 0:
                    neighbors.append(grid[i][j - 1])
                if j < n - 1:
                    neighbors.append(grid[i][j + 1])
                neighbor_mean = sum(neighbors) / len(neighbors)

                s = grid[i][j]
                new_s = (
                    s
                    + diff * (neighbor_mean - s)
                    + macro_coupling * (w - s)
                    + forcing_scale * f
                    + random.uniform(-noise, noise)
                )
                new_grid[i][j] = max(-1.0, min(1.0, new_s))

        total = 0.0
        for i in range(n):
            total += sum(new_grid[i])
        mean_a = total / (n * n)

        w = w + attention_scale * mean_a + forcing_scale * f - damping * w + random.uniform(-noise, noise)

        if assimilation_series is not None and t < len(assimilation_series):
            target = assimilation_series[t]
            if target is not None:
                w = w + assimilation_strength * (target - w)

        grid = new_grid
        w_series.append(w)
        if _store_grid:
            grid_series.append([row[:] for row in grid])

    return {
        "w": w_series,
        "grid": grid_series,
        "forcing": forcing,
    }
