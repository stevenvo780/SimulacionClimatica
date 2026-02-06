# 04_3 Experimento: La Dinámica Bursátil (SPY)

## 1. Configuración del Test (Setup)
*   **Dataset:** Precios históricos del SPY (Yahoo Finance), 1990-2024.
*   **Target:** Intentar modelar el mercado como un sistema híbrido con inercia macro.

## 2. El Desafío Técnico
A diferencia del clima, el mercado no tiene leyes físicas fijas. La "eficacia causal" en finanzas es psicológica y social.

## 3. Hallazgos (The Failure Analysis)
El experimento falló al intentar mantener un **EDI > 0.30**. Esto sugiere dos posibilidades:
1.  El SPY no es un Hiperobjeto estructurado.
2.  Nuestra ecuación macro es demasiado simple para capturar la complejidad financiera.

## 4. Valor para la Tesis
Este caso sirve como "Grupo de Control". Demuestra que nuestro método de validación C1-C5 tiene capacidad de discriminación: no valida cualquier cosa que le echemos, solo lo que realmente tiene estructura de Hiperobjeto.
