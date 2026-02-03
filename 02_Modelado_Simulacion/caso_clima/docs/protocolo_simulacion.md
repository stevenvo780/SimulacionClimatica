# Protocolo de Simulacion (Clima Regional)

## 1. Definicion de escenario
- Objetivo: demostrar persistencia estructural y no-localidad funcional.
- Delimitacion: region funcional, cohesion interna > externa.

## 2. Diseno de agentes
- Agentes: celdas con `T` y `H`.
- Reglas: difusion local + forcing exogeno + acople macro.

## 3. Inicializacion
- Grilla con distribucion inicial y semillas documentadas.
- Parametros base definidos en `src/validate.py`.
- Split entrenamiento/validacion: 1990-2010 / 2011-2024.

## 4. Ejecucion
- Escenario base y contrafactuales.
- Criterio de paro: estabilidad de patrones (varianza de `T_bar` estabilizada) y costo marginal > beneficio.
- Se usa nudging con observacion rezagada (t-1) para evaluacion de corto plazo.

## 5. Evaluacion
- Comparacion con serie sintetica.
- C1-C5 obligatorios.
