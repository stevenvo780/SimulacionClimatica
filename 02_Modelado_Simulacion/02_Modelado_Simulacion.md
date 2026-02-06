# 02 Modelado y Simulación: La Clase HybridModel

Para validar la Hipótesis H1, hemos implementado un framework de simulación basado en el acoplamiento de escalas. Aquí está la arquitectura lógica del motor:

## 1. Arquitectura de Clases (Pseudocódigo)

```python
class HybridModel:
    def __init__(self, micro_params, macro_params):
        self.micro = AgentBasedModel(micro_params)  # El "Suelo" (Píxeles)
        self.macro = DifferentialEquation(macro_params) # El "Satélite" (Tendencia)
        self.edi = 0.0  # Índice de Emergencia

    def step(self, t, real_data=None):
        # PASO 1: El Macro dicta la tendencia teórica
        macro_target = self.macro.predict(t)
        
        # PASO 2: El Micro simula interacciones locales
        self.micro.diffuse()
        
        # PASO 3: NUDGING (La eficacia causal de H1)
        # Aplicamos la "fuerza macro" sobre cada agente local
        self.micro.apply_nudging(macro_target, strength=0.4)
        
        # PASO 4: ASIMILACIÓN (Opcional)
        if real_data:
            self.micro.assimilate(real_data[t])

    def evaluate_emergency(self, results_full, results_reduced):
        # Cálculo del EDI para blindar la tesis
        self.edi = (rmse(results_reduced) - rmse(results_full)) / rmse(results_reduced)
        return self.edi
```

## 2. El Proceso de "Nudging"
No es un simple ajuste estadístico; es la representación computacional de la **Causalidad Descendente**. El sistema global (Macro) restringe los grados de libertad de los agentes locales (Micro), forzando la emergencia de patrones que el azar no explicaría.
