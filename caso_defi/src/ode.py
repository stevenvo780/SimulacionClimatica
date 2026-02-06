import random

def simulate_ode(params, steps, seed):
    """
    Modelo Macro: Dinámica de Precio con impacto de liquidaciones.
    """
    random.seed(seed)
    alpha = params["ode_alpha"]
    beta = params["ode_beta"]
    lambda_impact = params.get("lambda_impact", 0.05) # Impacto de liquidaciones en precio
    noise = params["ode_noise"]

    price = params["p0"]
    price_series = []
    
    # Serie de forzamiento externo (ej. tendencia del mercado global)
    forcing = params["forcing_series"]
    liquidation_pressure = params.get("liquidation_series", [0.0] * steps)

    for t in range(steps):
        f = forcing[t]
        s = liquidation_pressure[t]
        
        # El precio cae proporcionalmente a las liquidaciones (S)
        price = price + alpha * (f - beta * price) - lambda_impact * s + random.uniform(-noise, noise)
        price_series.append(max(0.1, price))

    return {
        "price": price_series,
        "forcing": forcing,
    }
