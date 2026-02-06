# Validacion C1-C5 (Finanzas Globales)

## C1 Convergencia
- Fase sintetica: ABM y ODE deben ajustar la serie sintetica con error bajo umbral.
- Fase real: ABM y ODE deben ajustar la serie real con error bajo umbral.
- Datos reales: SPY (1990-2024), cierre mensual.
- Umbral definido por caso: `0.6 * sigma` del conjunto de validacion.

## Verificacion (escenario controlado)
- La fase sintetica funciona como escenario simple con resultado conocido.
- Si falla, el modelo se invalida antes de pasar a datos reales.

## C2 Robustez
- Parametros se perturban en rango +/-10%.
- Resultados deben permanecer estables.

## C3 Replicacion
- Dos semillas/condiciones iniciales distintas.
- Se espera misma conclusion cualitativa (persistencia y no-localidad).

## C4 Validez
- Interna: reglas causales coherentes.
- Externa: respuesta a forcing alterno.
- Constructiva: correspondencia concepto-indicador documentada.

## C5 Incertidumbre explicita
- Sensibilidad reportada en `outputs/metrics.json`.
- Limites y supuestos declarados en `outputs/report.md`.

## Emergencia fuerte (criterio operativo)
- Se compara el modelo completo vs reducido (sin acople macro y sin nudging).
- La degradacion debe superar `0.2 * sigma` del conjunto de validacion.
