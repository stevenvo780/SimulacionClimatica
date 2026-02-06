import random
import numpy as np

def simulate_ode(params, steps, seed):
    """
    Modelo Macro: DDE (Delay Differential Equation) para precios de fletes.
    dP/dt = alpha * (Demanda(t) - Suministro(t-tau))
    """
    random.seed(seed)
    np.random.seed(seed)
    
    alpha = params["ode_alpha"]
    beta = params["ode_beta"] # Disipación (resolución de cuellos de botella)
    delay = int(params.get("delay_steps", 5))
    
    price = params.get("p0", 10.0)
    price_series = []
    
    # Historial para el delay
    # Inicialmente el suministro era igual a la demanda base
    supply_history = [10.0] * (delay + 1)
    
    backlog_series = params.get("backlog_series", [0.0] * steps)
    
    for t in range(steps):
        # Demanda Exógena (Base) + Endógena (Backlog Micro)
        # El backlog micro actúa como "panic buying" agregado
        current_demand = 10.0 + (backlog_series[t] * 0.1)
        
        # Suministro llega con retraso (lo que se envió hace 'delay' pasos)
        # Asumimos que el suministro responde al precio de hace 'delay' pasos
        # Si el precio era alto, se envió más barcos.
        past_supply_capacity = supply_history[-delay]
        
        # Dinámica de Precio: Escasez (Demanda > Suministro) sube precio
        delta_p = alpha * (current_demand - past_supply_capacity) - beta * (price - 10.0)
        
        price = price + delta_p + np.random.normal(0, 0.5)
        price = max(1.0, price)
        
        # La capacidad de suministro futura reacciona al precio actual (inversión en barcos)
        new_supply = 10.0 + (price - 10.0) * 0.5 
        supply_history.append(new_supply)
        
        price_series.append(price)

    return {
        "price": price_series
    }
