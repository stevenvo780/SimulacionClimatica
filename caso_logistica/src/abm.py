import random
import numpy as np

class SupplyNode:
    def __init__(self, id, role, capacity):
        self.id = id
        self.role = role # 'retailer', 'wholesaler', 'factory'
        self.inventory = 50.0
        self.backlog = 0.0
        self.capacity = capacity
        self.incoming_order = 0.0
        
    def step(self, demand, supply_in):
        # 1. Recibir suministro (limitado por capacidad de recepción)
        received = min(supply_in, self.capacity)
        self.inventory += received
        
        # 2. Satisfacer demanda
        total_demand = demand + self.backlog
        sold = min(self.inventory, total_demand)
        
        self.inventory -= sold
        self.backlog = total_demand - sold
        
        # 3. Calcular nuevo pedido (Regla de Pánico: Si hay backlog, pedir doble)
        # Target inventory = 50
        gap = 50.0 - self.inventory + self.backlog
        order = max(0, gap)
        
        if self.backlog > 10: 
            order *= 1.5 # Pánico
            
        return sold, order # Lo que entregué, Lo que pido

def simulate_abm(params, steps, seed):
    random.seed(seed)
    np.random.seed(seed)
    
    # Cadena Lineal Simple: Retail -> Wholesaler -> Factory
    retailer = SupplyNode("R", "retailer", capacity=100)
    wholesaler = SupplyNode("W", "wholesaler", capacity=80) # Cuello de botella leve
    factory = SupplyNode("F", "factory", capacity=60) # Cuello de botella grave
    
    # Macro Nudging: El "Precio Macro" afecta la capacidad (huelgas, falta de contenedores)
    macro_price_series = params.get("macro_price_series", [10.0] * steps)
    
    total_backlog_series = []
    stress_index_series = []
    
    # Delay de transporte (tubería)
    transit_w_r = [10.0] * 2 # Factory -> Wholesaler (2 pasos)
    transit_f_w = [10.0] * 4 # Wholesaler -> Retailer (4 pasos)
    
    for t in range(steps):
        # 1. Shock de Demanda Exógeno (Consumidor)
        # Simula el pico COVID: Demanda estable, luego explota, luego cae
        if steps * 0.3 < t < steps * 0.6:
            consumer_demand = np.random.normal(30, 5) # Shock
        else:
            consumer_demand = np.random.normal(10, 2)
            
        # 2. Efecto del Macro Precio en Capacidad (Si el flete es caro, la capacidad baja)
        current_macro_p = macro_price_series[t]
        capacity_factor = 1.0 / (1.0 + (current_macro_p - 10.0) * 0.05)
        factory.capacity = 60 * capacity_factor
        
        # 3. Flujo Aguas Arriba (Pedidos) y Aguas Abajo (Bienes)
        
        # Retailer Step
        r_supply_in = transit_w_r.pop(0)
        r_sold, r_order = retailer.step(consumer_demand, r_supply_in)
        
        # Wholesaler Step
        w_supply_in = transit_f_w.pop(0)
        w_sold, w_order = wholesaler.step(r_order, w_supply_in)
        
        # Factory Step (Supply infinito, pero limitado por capacidad de producción)
        f_sold, f_order = factory.step(w_order, 1000.0)
        
        # Envíos (Push to transit)
        transit_w_r.append(w_sold)
        transit_f_w.append(f_sold)
        
        # Métricas Agregadas
        sys_backlog = retailer.backlog + wholesaler.backlog + factory.backlog
        total_backlog_series.append(sys_backlog)
        
        # Stress Index (Inventario promedio invertido)
        avg_inv = (retailer.inventory + wholesaler.inventory + factory.inventory) / 3
        stress = max(0, 100 - avg_inv) # Si inventario es 0, estrés es 100
        stress_index_series.append(stress)
        
    return {
        "backlog": total_backlog_series,
        "stress": stress_index_series
    }
