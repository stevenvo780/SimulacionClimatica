# 01_16 Gobernanza de Datos: Limpieza y Ética

No todos los datos son válidos. Aplicamos filtros de calidad:

1.  **Filtro de Nulos:** Si una estación meteorológica tiene más del 15% de datos faltantes, se descarta (`drop_na`).
2.  **Normalización:** Llevamos todos los datos a escalas comparables para que la "Goma Elástica" (Nudging) no se rompa por diferencias de magnitud.
3.  **Ética:** Solo usamos datos de acceso público y abierto (Open Data).
