# Component 9: Verification and Evaluation Plan

**Responsible Person**: Ivan Kuznetsov (*Machine Learning & Spatial Data Science Engineer*)

---

## 1. Overview and Evaluation Philosophy
To scientifically demonstrate the achievement of the project aim, our verification strategy encompasses three complementary layers:
1. **Machine Learning Model Accuracy & Generalization**: Rigorous spatial cross-validation and standard thermodynamic regression metrics.
2. **Benchmarking against Baseline Solutions**: Quantifiable performance gain over traditional spatial and statistical baselines.
3. **Software Quality & System Verification**: Automated test suites for data pipelines, indices calculation, and API response SLAs.

---

## 2. Machine Learning Evaluation Metrics

Let $y_i$ be the ground-truth observed satellite Land Surface Temperature (LST) for spatial cell $i$, $\hat{y}_i$ be the predicted temperature, and $\bar{y}$ be the mean observed temperature across $N$ test cells:

1. **Coefficient of Determination ($R^2$)**:
   $$R^2 = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2}$$
   *Target Threshold*: $R^2 \ge 0.75$.

2. **Root Mean Squared Error (RMSE)**:
   $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2}$$
   *Target Threshold*: $\text{RMSE} \le 1.8^\circ\text{C}$.

3. **Mean Absolute Error (MAE)**:
   $$\text{MAE} = \frac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i|$$
   *Target Threshold*: $\text{MAE} \le 1.4^\circ\text{C}$.

---

## 3. Spatial Cross-Validation Strategy (Spatial K-Fold)
Standard random train/test splitting leads to overly optimistic performance due to spatial autocorrelation (Tobler's First Law of Geography: nearby pixels have similar temperatures).  
To prevent data leakage:
- **Spatial Block Partitioning**: The city of Astana is divided into $5\text{ km} \times 5\text{ km}$ spatial blocks.
- **K-Fold Block Split**: Entire geographic blocks are assigned exclusively to either the training set or the validation set (5-Fold Spatial CV).
- **Temporal Hold-Out**: The model is trained on multi-spectral summer scenes from 2021–2024 and evaluated against unseen summer 2025/2026 scenes.

---

## 4. Baseline Solutions for Comparison

We compare our proposed Gradient Boosted / Graph model against two established baselines:

| Baseline Model | Description | Expected Limitations | Target Improvement |
|---|---|---|---|
| **Baseline 1: Historical Mean Persistence Model** | Assigns the historical 5-year average summer temperature to each land parcel. | Cannot reflect new construction, vegetation changes, or localized cooling interventions. | Our model must reduce RMSE by at least **35%** relative to Baseline 1. |
| **Baseline 2: Ordinary Least Squares (OLS) Spatial Regression** | Classical linear regression using NDVI and distance to water. | Cannot model threshold non-linearities (e.g., minimum park size needed for cooling effect). | Our model must increase $R^2$ by at least **0.15** points and reduce RMSE by **20%** relative to OLS. |

---

## 5. Software Verification and Automated Testing Plan

### Automated Test Suite
- **Unit Tests (`tests/test_ml.py`)**:
  - Verification of mathematical edge-cases: zero division protection in NDVI/NDWI when pixel values are zero.
  - Radiance-to-temperature conversion tests against known physical constants ($h, c, k$).
- **API Tests (`tests/test_api.py`)**:
  - HTTP 200 checks on `/api/v1/health` and `/api/v1/layers`.
  - Schema validation for POST `/api/v1/forecast` and `/api/v1/optimize`.
  - Performance SLA verification: response generation within $< 3.0$ seconds.

### Execution Command
```bash
python -m unittest discover tests/
```

---

## 6. Verification Traceability Matrix

| Requirement | Success Metric | Verification Method |
|---|---|---|
| **FR-02 (Index Calculation)** | Valid NDVI $[-1, 1]$, LST in Celsius | Automated unit tests (`test_ml_unittest.py`) |
| **FR-04 (LST Prediction)** | $\text{RMSE} \le 1.8^\circ\text{C}$, $R^2 \ge 0.75$ | 5-Fold Spatial Cross-Validation script |
| **FR-06 (Optimization)** | Valid Pareto frontier with $\Delta T \le -1.5^\circ\text{C}$ | Algorithmic test with budget bounds check |
| **NFR-02 (Latency)** | Latency $< 3.0\text{ s}$ under concurrent requests | Automated HTTP test client latency assertion |
| **NFR-05 (Reproducibility)** | 100% test pass rate on clean clone | Automated CI test run via GitHub Actions |
