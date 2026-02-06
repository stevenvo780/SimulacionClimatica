# 04_1 Estructura de los Casos de Estudio

Para que los experimentos sean comparables, todos deben tener el mismo "esqueleto" o estructura de datos.

## 1. El Dataset
Cada caso debe definir su origen (API), su rango temporal y sus variables (ej. Temperatura, Precio, Co²).

## 2. La Configuración (Setup)
*   **Tamaño de Rejilla:** ¿Cuántos agentes vamos a simular?
*   **Parámetros de Calibración:** Los valores óptimos encontrados para que el modelo no explote.

## 3. El Reporte de Salida
Todos generan un `report.md` que resume si pasaron o no el examen C1-C5.
