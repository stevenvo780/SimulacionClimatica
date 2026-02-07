import random


def simulate_ode(params, steps, seed):
    random.seed(seed)
    alpha = params["ode_alpha"]
    beta = params["ode_beta"]
    noise = params["ode_noise"]

    forcing = params["forcing_series"]
    x = params["x0"]
    x_series = []
    assimilation_series = params.get("assimilation_series")
    assimilation_strength = params.get("assimilation_strength", 0.0)

    for t in range(steps):
        f = forcing[t]
        x = x + alpha * (f - beta * x) + random.uniform(-noise, noise)
        if assimilation_series is not None and t < len(assimilation_series):
            target = assimilation_series[t]
            if target is not None:
                x = x + assimilation_strength * (target - x)
        x_series.append(x)

    return {
        "x": x_series,
        "forcing": forcing,
    }
