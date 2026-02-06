# 03_4 Métricas de Validación: El Cuadro de Mandos

Aquí definimos los "sensores" que nos dicen si el sistema está funcionando bien.

## 1. RMSE (Error de Puntería)
Mide qué tan lejos estamos del dato real. 
*   **Analía:** Si tiras un dardo, el RMSE es la distancia en milímetros desde el centro.

## 2. Varianza (Fidelidad del Ritmo)
¿El modelo tiene la misma energía que la realidad? Si el clima real sube y baja bruscamente, el modelo no puede ser una línea suave y plana. Debe "vibrar" con la misma intensidad.

## 3. Coeficiente de Correlación
¿El modelo sube cuando la realidad sube? Si el clima real se calienta y el modelo se enfría, la correlación será negativa y el modelo será descartado por error lógico.
