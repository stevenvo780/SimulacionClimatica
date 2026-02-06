# 01_05 Pipeline de Ejecución: El Flujo de Trabajo

Este es el diagrama de flujo de cómo se procesa una simulación en esta tesis.

1.  **Fetch:** `data.py` descarga los CSV de Meteostat o yFinance.
2.  **Process:** `validate.py` instancia los modelos ABM y ODE.
3.  **Loop:** El tiempo avanza mes a mes, ejecutando los 3 pasos de cálculo (Calendario, Vecindario, Goma Elástica).
4.  **Export:** Se generan los archivos `metrics.json` y `report.md`.
