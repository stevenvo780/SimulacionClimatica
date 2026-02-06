import random
import numpy as np

def simulate_abm(params, steps, seed):
    """
    Modelo Micro: Agentes con Cascada de Liquidación (Versión de Estrés Garantizada).
    """
    random.seed(seed)
    np.random.seed(seed)
    
    num_agents = params.get("num_agents", 100)
    price = params["p0"]
    
    agents = []
    for _ in range(num_agents):
        # Escalar deuda proporcional al precio actual para garantizar fragilidad
        # Si P=2000, Deuda ~1800-1900.
        debt = random.uniform(0.8 * price, 0.95 * price)
        # Colateral = 1.0 unidades. Health Factor = (1 * P) / D. 
        # Si P cae por debajo de D * 1.05, liquidación.
        agents.append({"collateral": 1.0, "debt": debt, "active": True})

    price_series = []
    liquidation_volume_series = []
    forcing = params["forcing_series"]
    
    alpha = params["ode_alpha"]
    beta = params["ode_beta"]
    lambda_impact = params.get("lambda_impact", 0.1)

    for t in range(steps):
        f = forcing[t]
        current_selling_pressure = 0
        
        # 1. Liquidaciones
        for agent in agents:
            if not agent["active"]:
                continue
            
            health = (agent["collateral"] * price) / agent["debt"]
            if health < 1.05: 
                agent["active"] = False
                current_selling_pressure += agent["collateral"]
        
        # 2. Impacto masivo en el precio (feedback loop)
        # Multiplicamos el impacto por un factor de escala para ver el "abismo"
        price = price + alpha * (f - beta * price) - (lambda_impact * current_selling_pressure * 10) + random.uniform(-1, 1)
        price = max(0.1, price)
        
        price_series.append(price)
        liquidation_volume_series.append(current_selling_pressure)

    return {
        "price": price_series,
        "liquidations": liquidation_volume_series,
        "forcing": forcing
    }
