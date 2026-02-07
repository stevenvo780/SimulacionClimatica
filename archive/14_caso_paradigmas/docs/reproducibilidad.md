# Reproducibilidad (Paradigmas Cientificos)

## Versionado
- Repositorio principal con commit hash registrado en `metrics.json`.

## Entorno
- Python 3.10+
- Dependencias: `numpy`, `pandas`, `requests`.

## Sensibilidad
- Se reportan min/max de medias bajo perturbaciones de parametros.

## Datos
- Fuente OpenAlex, cache local en `data/openalex_paradigms.csv`.
- Para asegurar estabilidad, se guarda la serie agregada anual.
