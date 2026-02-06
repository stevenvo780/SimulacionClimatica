# 04_2 Experimento: El Hiperobjeto Climatológico

## 1. Configuración del Test (Setup)
*   **Dataset:** Temperaturas medias mensuales (Meteostat), 1990-2024.
*   **Target:** Demostrar que la "Goma Elástica" (Nudging) entre la tendencia global y la rejilla local es necesaria.

## 2. Parámetros Técnicos
*   `grid_size`: 10x10 agentes.
*   `nudging_strength`: 0.4 (Fuerza del acoplamiento).
*   `diffusion_rate`: 0.2 (Comunicación entre vecinos).

## 3. Resultados Contrastados
El experimento arrojó un **EDI de 0.45**, lo que significa que el 45% de la precisión del modelo depende directamente de la existencia de la estructura macro (el Hiperobjeto). Este resultado es la prueba empírica más sólida de la tesis.

## 4. Visualización de la Emergencia
El gráfico de resultados muestra cómo la rejilla de agentes, que inicialmente era caótica, se organiza siguiendo el "ritmo" dictado por la ecuación macro, pero manteniendo variaciones locales realistas.
