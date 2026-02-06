# Protocolo de Simulacion (Epidemiologia)

## 1. Definicion de escenario
- Objetivo: demostrar persistencia, no-localidad funcional y emergencia en incidencia agregada.
- Delimitacion: serie global (World) como proxy del sistema.

## 2. Diseno de agentes
- Agentes: estados S/I/R con contagio local.
- Reglas: probabilidad de contagio + recuperacion + acople macro.

## 3. Inicializacion
- Grilla con distribucion inicial y semillas documentadas.
- Parametros base definidos en `src/validate.py`.
- Split sintetica: 2010-2016 / 2017-2020.
- Split real: 2020-2021 / 2022-2023.

## 4. Ejecucion
- Escenario base y contrafactuales.
- Criterio de paro: estabilidad de indicadores y costo marginal > beneficio.
- Se usa nudging con observacion del mismo periodo (t) para evaluacion de corto plazo.

## 5. Evaluacion
- Comparacion en dos fases:
- Fase sintetica: verificacion interna y calibracion base.
- Fase real: evaluacion final con datos reales.
- C1-C5 obligatorios.
