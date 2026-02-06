# Protocolo de Simulacion (Wikipedia)

## 1. Definicion de escenario
- Objetivo: demostrar persistencia, no-localidad funcional y emergencia en atencion agregada.
- Delimitacion: cluster de articulos (clima) como proxy del sistema.

## 2. Diseno de agentes
- Agentes: celdas con atencion `A`.
- Reglas: difusion local + forcing exogeno + acople macro.

## 3. Inicializacion
- Grilla con distribucion inicial y semillas documentadas.
- Parametros base definidos en `src/validate.py`.
- Split sintetica: 2000-2009 / 2010-2019.
- Split real: 2015-2019 / 2020-2024.

## 4. Ejecucion
- Escenario base y contrafactuales.
- Criterio de paro: estabilidad de indicadores y costo marginal > beneficio.
- Se usa nudging con observacion del mismo periodo (t) para evaluacion de corto plazo.

## 5. Evaluacion
- Comparacion en dos fases:
- Fase sintetica: verificacion interna y calibracion base.
- Fase real: evaluacion final con datos reales.
- C1-C5 obligatorios.
