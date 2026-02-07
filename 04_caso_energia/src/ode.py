import random


def simulate_ode(params, steps, seed):
    random.seed(seed)
    alpha = params["ode_alpha"]
    beta = params["ode_beta"]
    noise = params["ode_noise"]

    forcing = params["forcing_series"]
    e = params["e0"]
    e_series = []
    assimilation_series = params.get("assimilation_series")
    assimilation_strength = params.get("assimilation_strength", 0.0)

    for t in range(steps):
        f = forcing[t]
        e = e + alpha * (f - beta * e) + random.uniform(-noise, noise)
        if assimilation_series is not None and t < len(assimilation_series):
            target = assimilation_series[t]
            if target is not None:
                e = e + assimilation_strength * (target - e)
        e_series.append(e)

    return {
        "e": e_series,
        "forcing": forcing,
    }
