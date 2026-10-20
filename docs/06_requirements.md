# Component 6: Requirements Specification (SRS)

**Responsible Persons**: Ivan Kuznetsov (NFR & ML Acceptance) & Zhetpis Baigulov (FR, API & MoSCoW)

---

## 1. Overview and MoSCoW Prioritization Framework
This specification details the functional (FR) and non-functional (NFR) requirements for the Intelligent GBI & UHI Decision Support GIS. Each requirement is assigned a priority under the MoSCoW standard:
- **Must Have (M)**: Mandatory for Pre-Defense / Minimal Viable Product.
- **Should Have (S)**: High priority, scheduled for subsequent sprint milestones.
- **Could Have (C)**: Desirable feature if time and computational resources permit.
- **Won't Have (W)**: Explicitly deferred beyond current diploma scope.

---

## 2. Functional Requirements (FR)

| Req ID | Priority | Requirement Description | Acceptance Criteria & Verification Method |
|---|---|---|---|
| **FR-01** | **Must** | **Satellite Data Ingestion**: The system must ingest multi-spectral satellite rasters (Landsat 8/9, Sentinel-2) covering Astana metropolitan bounds. | Verification: Automated script downloads or streams tiles with cloud cover $< 10\%$ for summer months (June–August). |
| **FR-02** | **Must** | **Spectral Index Calculation**: The system must compute NDVI, NDWI, NDBI, and LST (Land Surface Temperature) from calibrated bands. | Verification: Unit tests in `tests/test_ml.py` verify mathematical output bounds (NDVI/NDWI $\in [-1, 1]$, LST in Celsius $\in [15, 55]$). |
| **FR-03** | **Must** | **Spatial Heatmap API**: Backend must serve raster/vector thermal anomaly layers as GeoJSON or XYZ raster tiles. | Verification: GET `/api/v1/layers` returns list of active layers with HTTP 200 and valid JSON schema. |
| **FR-04** | **Must** | **Microclimate Prediction**: Given a user-defined district bounding box or modified land-cover vector, the system must predict projected LST. | Verification: POST `/api/v1/forecast` returns mean temperature and identified hotspot clusters within 3 seconds. |
| **FR-05** | **Should** | **Graph Network Analysis**: Model existing parks and water bodies as graph nodes connected by street trees and open spaces. | Verification: NetworkX script computes betweenness centrality and ecological connectivity index for city green spaces. |
| **FR-06** | **Should** | **GBI Spatial Optimization**: System must suggest top-N candidate parcels for tree planting or water retention to maximize cooling under a spatial budget. | Verification: POST `/api/v1/optimize` returns prioritized list of cadastral parcel IDs and projected $\Delta LST$ reduction. |
| **FR-07** | **Must** | **Interactive Web Map UI**: Front-end map must allow toggling thermal layers, zooming to city districts, and inspecting pixel/parcel temperatures. | Verification: Web browser displays map canvas (Mapbox GL/Leaflet) with layer toggle controls and tooltip inspection. |
| **FR-08** | **Could** | **Scenario Export**: Export generated optimization scenarios to GeoJSON and PDF summary report. | Verification: Download button generates valid standard `.geojson` file compatible with QGIS. |

---

## 3. Non-Functional Requirements (NFR)

| Req ID | Category | Requirement Description | Verification Metric / Threshold |
|---|---|---|---|
| **NFR-01** | **Accuracy (ML)** | The surface temperature regression model must accurately predict observed satellite LST on held-out test data. | Metric: Coefficient of determination $R^2 \ge 0.75$; Root Mean Squared Error $\text{RMSE} \le 1.8^\circ\text{C}$. |
| **NFR-02** | **Performance (API)** | Cached spatial layer queries must respond with low latency to ensure smooth web navigation. | Metric: 95th percentile response time $< 500\text{ ms}$ for layer metadata; $< 3.0\text{ s}$ for dynamic ML inference. |
| **NFR-03** | **Data Integrity** | Geographic coordinates must adhere to standardized spatial reference systems. | Metric: All vector layers stored in WGS84 (EPSG:4326) or UTM Zone 42N (EPSG:32642) for metric distance calculations. |
| **NFR-04** | **Modularity & Maintainability** | Backend and ML pipeline must follow clean architecture with loose coupling. | Metric: ML inference module runnable independently via CLI/library; backend communicates through typed Pydantic models. |
| **NFR-05** | **Reproducibility** | Entire environment, dependencies, and test suite must be reproducible on clean machines. | Metric: `docker build` succeeds without errors; `pytest` passes 100% of test assertions. |
| **NFR-06** | **Security & Secrets** | No API keys, credentials, or confidential database URLs committed to version control. | Metric: Pre-commit git hooks and `.gitignore` prevent committing `.env` or credential files. |
