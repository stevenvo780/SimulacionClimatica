# 02_1 Arquitectura de Modelos: El Enfoque de los Dos Niveles

Para entender un sistema complejo (un Hiperobjeto), nuestra arquitectura no usa una sola visión, sino dos que trabajan en equipo. 

## 1. El Nivel Micro (La vista desde el suelo)
Imagina que estamos en un bosque y miramos árbol por árbol. Cada árbol interactúa con sus vecinos más cercanos (les da sombra, les pasa nutrientes).
*   **En la simulación:** Lo llamamos **ABM** (Modelo Basado en Agentes). Dividimos el mapa en una rejilla de celdas.
*   **La lógica:** Cada celda solo sabe qué temperatura tienen sus vecinas. No sabe nada del mundo exterior.

## 2. El Nivel Macro (La vista desde el satélite)
Ahora imagina que miras el bosque desde un avión. Ya no ves árboles individuales, ves una mancha verde. Aquí lo que importa es el clima general: si es verano, si hay sequía, o si el planeta se está calentando.
*   **En la simulación:** Lo llamamos **ODE** (Ecuación Diferencial). Es una fórmula que dicta la tendencia general.

## 3. ¿Por qué unirlos? (El Modelo Híbrido)
Si solo miramos los árboles (Micro), perdemos de vista las estaciones. Si solo miramos el bosque desde el avión (Macro), perdemos de vista los incendios locales. 

La magia ocurre cuando los conectamos. En lugar de una fórmula matemática compleja, usamos esta lógica:

```python
# Así se hablan los dos niveles:
nueva_temperatura_celda = (
    temperatura_actual +
    influencia_de_vecinos +      # Lo que pasa cerca (Micro)
    influencia_del_calendario +  # Lo que dicta el clima global (Macro)
    ajuste_de_error               # Un pequeño empujón para no perder el rumbo
)
```

Esta arquitectura híbrida es la que nos permite pasar las pruebas de validación, porque captura tanto el detalle pequeño como la tendencia grande.
