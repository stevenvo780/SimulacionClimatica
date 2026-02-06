# 04_6 Plan de Caso: Contaminacion del Aire (PM2.5)

## Objetivo
- Ejecutar un caso de contaminacion del aire con dos fases: sintetica (verificacion interna) y real (evaluacion final).

## Fuente de datos reales
- World Bank API: indicador `EN.ATM.PM25.MC.M3` (exposicion promedio a PM2.5).
- Serie anual global (`WLD`).

## Metodologia
- Dos modelos no isomorfos: ABM (micro) + ODE (macro).
- Variable puente: nivel agregado de contaminacion.
- Indicadores: symploke, no-localidad, persistencia, emergencia.
- Criterios C1–C5 obligatorios.

## Fases y splits
- Fase sintetica: 1980-2019, split 2000.
- Fase real: 1990-2020, split 2006.

## Entregables
- Reporte reproducible (`report.md`) y metricas (`metrics.json`).
- Validacion en 03 y caso ejecutado en 04.
- Actualizar indices y matriz 00–01.
