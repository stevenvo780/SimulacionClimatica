import math
import random


def forcing_series(steps, base, trend, seasonal_amp, seasonal_period):
    series = []
    for t in range(steps):
        seasonal = seasonal_amp * math.sin(2.0 * math.pi * t / seasonal_period)
        series.append(base + trend * t + seasonal)
    return series


def simulate_ode(params, steps, seed):
    random.seed(seed)
    alpha = params["ode_alpha"]
    beta = params["ode_beta"]
    noise = params["ode_noise"]

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

    tbar = params["t0"]
    tbar_series = []
    assimilation_series = params.get("assimilation_series")
    assimilation_strength = params.get("assimilation_strength", 0.0)

    for t in range(steps):
        f = forcing[t]
        
        # TRADUCCIÓN PARA INFORMÁTICOS (Balance Energético):
        # tbar = tbar + alpha * (input - output) + noise
        # alpha: Velocidad de reacción del sistema.
        # (f - beta * tbar): Diferencia entre energía que entra (f) y la que se disipa (beta * tbar).
        tbar = tbar + alpha * (f - beta * tbar) + random.uniform(-noise, noise)
        
        # NUDGING: Si hay datos reales, aplicamos un "ajuste manual" para corregir el rumbo.
        if assimilation_series is not None and t < len(assimilation_series):
            target = assimilation_series[t]
            if target is not None:
                tbar = tbar + assimilation_strength * (target - tbar)
        tbar_series.append(tbar)

    return {
        "tbar": tbar_series,
        "forcing": forcing,
    }
