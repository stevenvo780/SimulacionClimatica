import math
import random


def forcing_series(steps, base, trend, seasonal_amp, seasonal_period):
    series = []
    for t in range(steps):
        seasonal = seasonal_amp * math.sin(2.0 * math.pi * t / seasonal_period)
        series.append(base + trend * t + seasonal)
    return series


def simulate_abm(params, steps, seed):
    random.seed(seed)
    n = params["grid_size"]
    diff = params["diffusion"]
    noise = params["noise"]
    macro_coupling = params["macro_coupling"]
    forcing_scale = params.get("forcing_scale", 0.01)
    damping = params.get("damping", 0.02)
    assimilation_series = params.get("assimilation_series")
    assimilation_strength = params.get("assimilation_strength", 0.0)

    # Initialize grid
    grid = [[params["t0"] + random.uniform(-0.5, 0.5) for _ in range(n)] for _ in range(n)]
    hum = [[params["h0"] + random.uniform(-0.05, 0.05) for _ in range(n)] for _ in range(n)]

    if "forcing_series" in params:
        forcing = params["forcing_series"]
    else:
        forcing = forcing_series(
            steps,
            params["forcing_base"],
            params["forcing_trend"],
            params["forcing_seasonal_amp"],
            params["forcing_seasonal_period"],
        )

    tbar_series = []
    grid_series = []

    for t in range(steps):
        # Compute macro state
        total = 0.0
        for i in range(n):
            total += sum(grid[i])
        tbar = total / (n * n)

        # Update grid
        new_grid = [[0.0 for _ in range(n)] for _ in range(n)]
        new_hum = [[0.0 for _ in range(n)] for _ in range(n)]
        f = forcing[t]
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

                # Micro dynamics: diffusion + forcing + macro coupling + noise
                new_t = (
                    grid[i][j]
                    + diff * (neighbor_mean - grid[i][j])
                    + forcing_scale * f
                    + macro_coupling * (tbar - grid[i][j])
                    - damping * grid[i][j]
                    + random.uniform(-noise, noise)
                )

                # Humidity as a weakly coupled auxiliary variable
                new_h = hum[i][j] + 0.05 * (0.5 - hum[i][j]) + 0.001 * f

                new_grid[i][j] = new_t
                new_hum[i][j] = new_h

        # Optional assimilation (nudging) using lagged observations
        if assimilation_series is not None and t < len(assimilation_series):
            target = assimilation_series[t]
            if target is not None:
                for i in range(n):
                    for j in range(n):
                        new_grid[i][j] += assimilation_strength * (target - tbar)

        grid = new_grid
        hum = new_hum

        # Store snapshot and updated macro state
        total = 0.0
        for i in range(n):
            total += sum(grid[i])
        tbar_series.append(total / (n * n))
        grid_series.append([row[:] for row in grid])

    return {
        "tbar": tbar_series,
        "grid": grid_series,
        "forcing": forcing,
    }
