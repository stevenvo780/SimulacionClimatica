# 01_04 Auditoría y Reproducibilidad: Control de Versiones

En ciencia, como en el código, si no se puede reproducir, no existe.

## 1. Hashing de Datos
Cada dataset utilizado tiene un `hash` único. Si los datos cambian, el resultado de la tesis debe actualizarse.

## 2. Control de Semillas (Seeds)
Usamos semillas aleatorias fijas (`random.seed(42)`) para que cualquier programador pueda obtener exactamente los mismos gráficos que nosotros.

## 3. Entorno Replicable
Todo el código está diseñado para correr en contenedores o entornos controlados (como este CLI). La reproducibilidad es nuestro `commit` final.
