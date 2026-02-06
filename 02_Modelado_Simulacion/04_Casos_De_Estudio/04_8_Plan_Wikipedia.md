# 04_8 Plan de Caso: Wikipedia (Atencion)

## Objetivo
- Ejecutar un caso de atencion colectiva con dos fases: sintetica (verificacion interna) y real (evaluacion final).

## Fuente de datos reales
- Wikimedia Pageviews API.
- Serie mensual agregada de un cluster de articulos.

## Metodologia
- Dos modelos no isomorfos: ABM (micro) + ODE (macro).
- Variable puente: atencion agregada.
- Indicadores: symploke, no-localidad, persistencia, emergencia.
- Criterios C1–C5 obligatorios.

## Fases y splits
- Fase sintetica: 2000-2019, split 2010.
- Fase real: 2015-2024, split 2020.

## Entregables
- Reporte reproducible (`report.md`) y metricas (`metrics.json`).
- Validacion en 03 y caso ejecutado en 04.
- Actualizar indices y matriz 00–01.
