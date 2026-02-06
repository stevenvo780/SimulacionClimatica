# Protocolo de Simulacion (Energia Electrica)

## 1. Definicion de escenario
- Objetivo: demostrar persistencia, no-localidad funcional y emergencia en demanda agregada.
- Delimitacion: demanda nacional (GB) como proxy del sistema.

## 2. Diseno de agentes
- Agentes: celdas con demanda `D`.
- Reglas: difusion local + forcing exogeno + acople macro.

## 3. Inicializacion
- Grilla con distribucion inicial y semillas documentadas.
- Parametros base definidos en `src/validate.py`.
- Split sintetica: 2000-2009 / 2010-2019.
- Split real: 2015-2018 / 2019-2020.

## 4. Ejecucion
- Escenario base y contrafactuales.
- Criterio de paro: estabilidad de indicadores y costo marginal > beneficio.
- Se usa nudging con observacion del mismo periodo (t) para evaluacion de corto plazo.

## 5. Evaluacion
- Comparacion en dos fases:
- Fase sintetica: verificacion interna y calibracion base.
- Fase real: evaluacion final con datos reales.
- C1-C5 obligatorios.
