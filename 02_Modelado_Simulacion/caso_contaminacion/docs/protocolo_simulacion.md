# Protocolo de Simulacion (Contaminacion PM2.5)

## 1. Definicion de escenario
- Objetivo: demostrar persistencia, no-localidad funcional y emergencia en contaminacion agregada.
- Delimitacion: promedio global (WLD) como proxy del sistema.

## 2. Diseno de agentes
- Agentes: celdas con contaminacion `C`.
- Reglas: difusion local + forcing exogeno + acople macro.

## 3. Inicializacion
- Grilla con distribucion inicial y semillas documentadas.
- Parametros base definidos en `src/validate.py`.
- Split sintetica: 1980-1999 / 2000-2019.
- Split real: 1990-2005 / 2006-2022.

## 4. Ejecucion
- Escenario base y contrafactuales.
- Criterio de paro: estabilidad de indicadores y costo marginal > beneficio.
- Se usa nudging con observacion rezagada (t-1) para evaluacion de corto plazo.

## 5. Evaluacion
- Comparacion en dos fases:
- Fase sintetica: verificacion interna y calibracion base.
- Fase real: evaluacion final con datos reales.
- C1-C5 obligatorios.
