# 03_1 Estrategia de Validación: El Test de Aceptación

Después de construir el motor, tenemos que probarlo en la carretera. Esta sección describe nuestra estrategia para certificar que el sistema es válido.

## 1. El Rigor C1-C5
Cada caso de estudio (Clima, Finanzas, etc.) debe pasar por estas 5 estaciones de inspección técnica. No hay excepciones.

## 2. Comparación con la Realidad (Ground Truth)
No comparamos el modelo con "opiniones", lo comparamos con datos crudos:
*   Temperaturas reales medidas por estaciones.
*   Precios de cierre reales del mercado.

## 3. El Criterio del "Valor Añadido"
Si el modelo híbrido no es **significativamente mejor** que un modelo de estadística simple, la validación falla. Buscamos demostrar que la estructura del Hiperobjeto aporta información que no se puede obtener de otra manera.
