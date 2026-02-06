# 04_11 Caso de Estudio: Energia Electrica (Ejecutado)

## Contexto
- Fenomeno: demanda electrica agregada con shocks externos.
- Justificacion: evidencia distribuida y patrones recurrentes.

## Datos
- Fase sintetica: serie controlada 2000-2019 con estacionalidad.
- Fase real: OPSD GB load (mensual), 2015-2020.
- Archivos de resultados: `02_Modelado_Simulacion/caso_energia/report.md` y `02_Modelado_Simulacion/caso_energia/metrics.json`.

## Modelado
- Modelo micro: ABM lattice 2D con difusion local y acople macro.
- Modelo macro: ODE de balance agregado para demanda.
- Variable puente: `E` (demanda agregada) acopla micro y macro.

## Resultados
- Fase sintetica: `overall_pass = True`.
- Fase real: `overall_pass = True`.
- Convergencia en ambas fases bajo umbral `0.6 * sigma`.
- Symploke interna > externa, no-localidad funcional y persistencia verificadas.
- Emergencia: el modelo reducido degrada el error por encima del umbral.

## Criterio de aceptacion
- Cumplimiento C1-C5 y reglas de indicadores en ambas fases.

## Limites y criterio de paro
- Limites: serie 2015-2020 y uso de proxy GB.
- Criterio de paro: estabilidad de patrones y costo marginal > beneficio.
