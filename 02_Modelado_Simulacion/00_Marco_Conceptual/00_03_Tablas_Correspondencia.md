# 00_03 Tablas de Correspondencia: El Mapping de la Tesis

Para un programador, este es el archivo de configuración del **ORM (Object-Relational Mapping)**. Aquí decimos cómo un concepto abstracto ("Clase") se mapea a un dato real en la base de datos ("Métrica").

| Concepto Abstracto (Clase) | Indicador Operativo (Property) | Métrica Técnica (Value) |
| :--- | :--- | :--- |
| **No-localidad** | Distribución de varianza | `window_variance / global_variance` |
| **Emergencia Fuerte** | Degradación de error | `RMSE_reducido - RMSE_completo` |
| **Persistencia** | Estabilidad de régimen | `Hurst_exponent > 0.5` |
| **Symploke (Frontera)** | Cohesión de red | `Internal_link_density > External_noise` |

**Nota de Implementación:** Si no puedes llenar la tercera columna para un concepto, ese concepto es un "Bug" y debe ser eliminado del código de la tesis.
