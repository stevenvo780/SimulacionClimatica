# 02_5 Validación y Verificación: ¿Cómo sabemos si funciona?

No basta con que el modelo haga dibujos bonitos; tiene que ser científicamente válido. Para ello, usamos un examen de 5 puntos (C1-C5).

## 1. Verificación (¿Está bien programado?)
Antes de mirar la realidad, comprobamos que el código no tenga bugs.
*   **Prueba:** Corremos el modelo en un entorno controlado donde ya sabemos cuál debe ser la respuesta (Fase Sintética).
*   **Criterio:** Si el programa no da el resultado esperado en este escenario fácil, ni siquiera intentamos usar datos reales.

## 2. Validación (¿Se parece a la realidad?)
Aquí es donde comparamos los resultados del modelo con los datos históricos (ej. 1990-2024).

| Criterio | Nombre | Explicación sencilla |
| :--- | :--- | :--- |
| **C1** | Convergencia | ¿El dardo cayó cerca del centro de la diana (los datos reales)? |
| **C2** | Robustez | Si muevo un poco los parámetros, ¿el modelo sigue siendo estable? |
| **C3** | Replicación | Si lo corres tú en tu ordenador, ¿da el mismo resultado? |
| **C4** | Validez | ¿Las reglas del código tienen sentido físico (ej. el calor sube)? |
| **C5** | Incertidumbre | ¿Sabemos cuánto nos podemos estar equivocando? |

## 3. La Regla de Oro (Emergencia Fuerte)
Para que la tesis sea válida, el modelo híbrido **DEBE** ser mejor que el modelo simple. 

```python
# El examen final del modelo:
if error_modelo_hibrido < error_modelo_simple:
    print("Éxito: Se demuestra la existencia del Hiperobjeto (H1)")
else:
    print("Fallo: El nivel macro no es necesario para explicar este sistema")
```
