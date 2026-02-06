import random


def simulate_ode(params, steps, seed):
    random.seed(seed)
    alpha = params["ode_alpha"]
    beta = params["ode_beta"]
    noise = params["ode_noise"]

    forcing = params["forcing_series"]
    w = params["w0"]
    w_series = []
    assimilation_series = params.get("assimilation_series")
    assimilation_strength = params.get("assimilation_strength", 0.0)

    for t in range(steps):
        f = forcing[t]
        w = w + alpha * (f - beta * w) + random.uniform(-noise, noise)
        if assimilation_series is not None and t < len(assimilation_series):
            target = assimilation_series[t]
            if target is not None:
                w = w + assimilation_strength * (target - w)
        w_series.append(w)

    return {
        "w": w_series,
        "forcing": forcing,
    }
