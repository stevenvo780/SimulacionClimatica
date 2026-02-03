# Indicadores, Metricas y Reglas (Clima Regional)

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## Symploke (cohesion)
- Metrica: correlacion media de vecinos internos vs correlacion con forcing externo.
- Regla: cohesion interna > externa con diferencia positiva.

## Emergencia fuerte
- Metrica: error predictivo al eliminar acople macro.
- Regla: el modelo reducido incrementa el error por encima de umbral.

## No-localidad funcional
- Metrica: dominancia de fuentes (max share de influencia).
- Regla: ninguna fuente supera el umbral definido por caso.

## Persistencia estructural
- Metrica: estabilidad de regimen (varianza de `T_bar` en ventanas largas).
- Regla: estabilidad bajo perturbaciones razonables y comparable al regimen observado.

## Causalidad descendente debil
- Metrica: cambios en distribuciones micro al variar condiciones macro.
- Regla: diferencias micro significativas bajo cambios macro controlados.
