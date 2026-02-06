# 00_04 Ejercicios Filosóficos: Code Review Conceptual

Estos ejercicios no son reflexiones al aire, son **pruebas de escritorio** para verificar que nuestra lógica no tiene fugas de memoria conceptual.

## Ejercicio 1: El Test de la Caja Negra
*   **Escenario:** Si un modelo puramente estadístico (ej. una IA) predice el clima mejor que nuestro modelo híbrido, ¿sigue siendo real el hiperobjeto?
*   **Lógica de Programador:** Si una función externa `predict()` es más eficiente, nuestra implementación actual podría ser obsoleta (Deprecation). Debemos investigar si la IA está capturando la "Estructura" o solo "Correlaciones".

## Ejercicio 2: Refactorización de Fronteras
*   **Escenario:** ¿Dónde termina el "Clima Regional" y empieza el "Clima Global"?
*   **Lógica de Programador:** Es un problema de **encapsulamiento**. Definimos el `scope` mediante la métrica de Symploke. Si el acoplamiento es bajo, separamos en dos servicios distintos (Microservicios).
