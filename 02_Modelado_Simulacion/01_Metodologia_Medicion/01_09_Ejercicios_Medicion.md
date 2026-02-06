# 01_09 Ejercicios de Medición: Debugging Práctico

Estos son ejercicios para entrenar al investigador en la detección de errores en los datos.

## Ejercicio: El "Ghost in the Machine"
*   **Problema:** El modelo da un error de 0.1 (perfecto), pero el gráfico es una línea recta.
*   **Diagnóstico:** El modelo está "haciendo trampas" (Overfitting). Está leyendo el resultado futuro. 
*   **Solución:** Separar estrictamente los datos de entrenamiento de los de validación.
