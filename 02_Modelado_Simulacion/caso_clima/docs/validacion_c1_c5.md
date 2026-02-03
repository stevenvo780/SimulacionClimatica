# Validacion C1-C5 (Clima Regional)

## C1 Convergencia
- ABM y ODE deben ajustar la serie real con error bajo umbral.
- Datos reales regionales (Meteostat, CONUS, 1990-2024).
- Umbral definido por caso: `0.6 * sigma` del conjunto de validacion.

## C2 Robustez
- Parametros se perturban en rango +/-10%.
- Resultados deben permanecer estables (regimen y metricas).

## C3 Replicacion
- Dos semillas/condiciones iniciales distintas.
- Se espera misma conclusion cualitativa (persistencia y no-localidad).

## C4 Validez
- Interna: reglas causales coherentes.
- Externa: generalizacion a forcing alterno.
- Constructiva: correspondencia concepto-indicador documentada.

## C5 Incertidumbre explicita
- Sensibilidad reportada en `outputs/metrics.json`.
- Limites y supuestos declarados en `outputs/report.md`.

## Emergencia fuerte (criterio operativo)
- Se compara el modelo completo vs reducido (sin acople macro y sin nudging).
- La degradacion debe superar `0.2 * sigma` del conjunto de validacion.
