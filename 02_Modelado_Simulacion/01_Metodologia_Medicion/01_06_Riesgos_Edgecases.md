# 01_06 Riesgos y Edge Cases: Error Handling

Como en cualquier sistema complejo, las cosas pueden fallar. Aquí definimos cómo manejamos los errores de medición.

| Escenario (Error) | Tipo | Mitigación (Try/Catch) |
| :--- | :--- | :--- |
| **Sesgo de Selección** | `DataError` | Usar múltiples estaciones de datos (CONUS) para promediar. |
| **Divergencia del ABM** | `RuntimeError` | Ajustar la fuerza del "Nudging" (Paso 3 del algoritmo). |
| **Falta de Memoria Histórica** | `InputError` | Usar series sintéticas generadas por ODE para rellenar huecos. |
