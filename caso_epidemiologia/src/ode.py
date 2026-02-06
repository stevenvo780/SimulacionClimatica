import random


def simulate_seir(params, steps, seed):
    random.seed(seed)
    beta = params["beta"]
    sigma = params["sigma"]
    gamma = params["gamma"]
    noise = params["noise"]

    s = params.get("s0", 0.999)
    e = params.get("e0", 0.001)
    i = params.get("i0", 0.0)
    r = params.get("r0", 0.0)

    forcing = params["forcing_series"]
    incidence_series = []
    assimilation_series = params.get("assimilation_series")
    assimilation_strength = params.get("assimilation_strength", 0.0)

    for t in range(steps):
        f = forcing[t]
        beta_t = max(0.0, beta + f)
        new_e = beta_t * s * i
        new_i = sigma * e
        new_r = gamma * i

        s = max(0.0, s - new_e)
        e = max(0.0, e + new_e - new_i)
        i = max(0.0, i + new_i - new_r)
        r = max(0.0, r + new_r)

        inc = new_i + random.uniform(-noise, noise)
        if assimilation_series is not None and t < len(assimilation_series):
            target = assimilation_series[t]
            if target is not None:
                inc = inc + assimilation_strength * (target - inc)
        incidence_series.append(inc)

    return {
        "incidence": incidence_series,
        "forcing": forcing,
    }
