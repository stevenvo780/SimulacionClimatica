# 02_3 Protocolo de Simulación: El Algoritmo de Ejecución

Este es el manual de procedimientos para correr una simulación de principio a fin. Imaginalo como el `main()` de nuestro programa de investigación.

## 1. Fase de Setup (Inicialización)
Antes de empezar, cargamos la configuración:
*   **Parámetros:** Definimos la fuerza de la "goma elástica" (Nudging) y la tasa de difusión.
*   **Estado Inicial:** Ponemos la rejilla de agentes en un estado neutro o basado en el primer dato histórico.

## 2. El Bucle de Ejecución (The Tick)
La simulación avanza por pasos de tiempo (meses). En cada paso ocurre:

```python
for mes in linea_de_tiempo:
    # 1. El Macro predice la tendencia (Calendario)
    meta_global = modelo_ode.update() 
    
    # 2. Los Agentes interactúan (Vecindario)
    rejilla_abm.diffuse() 
    
    # 3. Sincronización (Nudging)
    rejilla_abm.apply_nudging(meta_global)
    
    # 4. Registro (Logging)
    guardar_estado_en_metrics_json()
```

## 3. Criterio de Parada
La simulación se detiene cuando llegamos al final de los datos históricos (ej. Diciembre 2024). En ese punto, el sistema genera automáticamente los artefactos de validación.
