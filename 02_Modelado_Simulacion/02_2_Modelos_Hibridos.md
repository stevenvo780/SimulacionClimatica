# 02_2 Modelos Híbridos: La conexión entre Escalas

En esta sección explicamos el "pegamento" que une lo pequeño con lo grande. En ciencia, esto se llama **Asimilación de Datos** o **Nudging**, pero podemos entenderlo con la analogía de la **Goma Elástica**.

## 1. El concepto de la Goma Elástica
Imagina que cada "agente" (cada cuadrito del mapa) está unido al promedio global por una goma elástica invisible.
*   Si el agente se calienta demasiado por su cuenta, la goma elástica lo tira un poco hacia el promedio global para que no se vuelva loco.
*   Si el promedio global cambia (llega el verano), la goma elástica tira de todos los agentes hacia arriba.

## 2. Traduciendo la matemática a lógica
En lugar de usar ecuaciones diferenciales parciales, el código hace este cálculo simple en cada paso de tiempo:

```python
def conectar_escalas(valor_local, valor_global):
    # Calculamos la distancia entre lo pequeño y lo grande
    error = valor_global - valor_local
    
    # Aplicamos la "fuerza de la goma" (un porcentaje del error)
    fuerza = 0.4  # Si es 0.4, corregimos un 40% del desvío
    
    return valor_local + (error * fuerza)
```

## 3. ¿Para qué sirve esto? (La Eficacia Causal)
Este pequeño cálculo es la prueba de nuestra Hipótesis **H1**. Demuestra que lo "Grande" (el sistema global) tiene poder para influir en lo "Pequeño" (los agentes individuales). Sin esta conexión, los modelos suelen fallar o dar resultados caóticos que no se parecen a la realidad.
