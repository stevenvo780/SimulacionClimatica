# Protocolo de Simulacion (Movilidad Urbana)

## 1. Definicion de escenario
- Objetivo: demostrar persistencia, no-localidad funcional y emergencia en movilidad agregada.
- Delimitacion: red de transporte urbano (proxy: MTA subway).

## 2. Diseno de agentes
- Agentes: celdas con flujo `F`.
- Reglas: difusion local + forcing exogeno + acople macro.

## 3. Inicializacion
- Grilla con distribucion inicial y semillas documentadas.
- Parametros base definidos en `src/validate.py`.
- Split sintetica: 2000-2009 / 2010-2019.
- Split real: 2020-2022 / 2023-2024.

## 4. Ejecucion
- Escenario base y contrafactuales.
- Criterio de paro: estabilidad de indicadores y costo marginal > beneficio.
- Se usa nudging con observacion rezagada (t-1) para evaluacion de corto plazo.

## 5. Evaluacion
- Comparacion en dos fases:
- Fase sintetica: verificacion interna y calibracion base.
- Fase real: evaluacion final con datos reales.
- C1-C5 obligatorios.
