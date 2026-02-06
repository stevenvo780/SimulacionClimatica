import random


def simulate_ode(params, steps, seed):
    random.seed(seed)
    alpha = params["ode_alpha"]
    beta = params["ode_beta"]
    noise = params["ode_noise"]

    forcing = params["forcing_series"]
    p = params["p0"]
    p_series = []
    assimilation_series = params.get("assimilation_series")
    assimilation_strength = params.get("assimilation_strength", 0.0)

    for t in range(steps):
        f = forcing[t]
        p = p + alpha * (f - beta * p) + random.uniform(-noise, noise)
        if assimilation_series is not None and t < len(assimilation_series):
            target = assimilation_series[t]
            if target is not None:
                p = p + assimilation_strength * (target - p)
        p_series.append(p)

    return {
        "p": p_series,
        "forcing": forcing,
    }
