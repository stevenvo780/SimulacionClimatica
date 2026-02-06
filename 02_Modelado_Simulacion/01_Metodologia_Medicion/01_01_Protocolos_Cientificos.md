# 01_01 Protocolos Científicos: El Pipeline de Validación

Para validar nuestra hipótesis (H1), seguimos un protocolo estricto que se asemeja a un pipeline de **CI/CD (Integración Continua / Despliegue Continuo)**. Si un modelo no pasa un paso, el build falla.

## Fase 1: Ingesta de Datos (Data Pipeline)
1.  **Source:** APIs climáticas/financieras (Meteostat, yFinance).
2.  **Clean:** Eliminación de outliers y normalización de series temporales.
3.  **Split:** Separamos los datos en `Training Set` (1990-2010) y `Validation Set` (2011-2024).

## Fase 2: Ejecución del Modelo Híbrido (The Engine)
Ejecutamos dos instancias paralelas para comparar:
*   **Instancia A (Híbrida):** `ABM.run()` acoplado con `ODE.run()`.
*   **Instancia B (Control/Reducida):** `ABM.run()` de forma aislada.

## Fase 3: Testing Unitario (C1-C5)
Cada simulación debe pasar los siguientes tests automáticos:

```javascript
test("C1: Convergencia", () => {
  const error = calculateRMSE(simResult, observedData);
  expect(error).toBeLessThan(threshold);
});

test("C2: Robustez (Stress Test)", () => {
  const params = getPerturbedParams(0.1); // Variamos 10%
  const newResult = runSimulation(params);
  expect(newResult).toBeStable();
});

test("C4: Validez (Logic Check)", () => {
  expect(model.logic).toComplyWith("Thermodynamics_v1.0");
});
```

## Fase 4: Despliegue del Reporte (Artifacts)
Si todos los tests pasan, el sistema genera automáticamente:
*   `metrics.json`: El dump de datos crudos.
*   `report.md`: El análisis interpretado para humanos.
*   **Gráficos:** Visualización de la emergencia detectada.

## Resumen del Workflow
1. `git clone` de los datos reales.
2. `npm install` de los parámetros calibrados.
3. `npm test` (Protocolo C1-C5).
4. `npm deploy` (Publicación en el Capítulo 04: Casos de Estudio).
