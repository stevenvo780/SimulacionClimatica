import random


def simulate_ode(params, steps, seed):
    random.seed(seed)
    alpha = params["ode_alpha"]
    beta = params["ode_beta"]
    noise = params["ode_noise"]

    forcing = params["forcing_series"]
    m = params["m0"]
    m_series = []
    assimilation_series = params.get("assimilation_series")
    assimilation_strength = params.get("assimilation_strength", 0.0)

    for t in range(steps):
        f = forcing[t]
        m = m + alpha * (f - beta * m) + random.uniform(-noise, noise)
        if assimilation_series is not None and t < len(assimilation_series):
            target = assimilation_series[t]
            if target is not None:
                m = m + assimilation_strength * (target - m)
        m_series.append(m)

    return {
        "m": m_series,
        "forcing": forcing,
    }
