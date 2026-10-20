# Component 5: Technology Comparison

**Responsible Persons**: 
- Remote Sensing & ML Architecture: Ivan Kuznetsov
- Backend & Spatial Database: Zhetpis Baigulov

---

## 1. Overview
To ensure robust engineering design, we evaluated reasonable alternatives across three foundational architectural decisions:
1. **Decision 1**: Remote Sensing Data Pipeline & Processing Engine.
2. **Decision 2**: Machine Learning Model for Surface Temperature & UHI Forecasting.
3. **Decision 3**: Backend Server Platform and Spatial Data Storage.

---

## 2. Decision 1: Remote Sensing Data Pipeline & Ingestion Engine

### Evaluated Alternatives
- **Alternative A: Google Earth Engine (GEE) Python API**
- **Alternative B: Sentinel Hub / Copernicus Data Space API + Local Rasterio**
- **Alternative C: Direct USGS EarthExplorer Bulk Downloads + GDAL CLI**

### Comparison Table

| Evaluation Criteria | Alt A: Google Earth Engine (GEE) | Alt B: Sentinel Hub / Copernicus | Alt C: USGS Direct / GDAL |
|---|---|---|---|
| **API Usability & Cloud Processing** | High (Cloud compute offloads heavy raster math) | High (Clean REST API, provides on-demand band math) | Low (Requires manual orchestration of large archives) |
| **Data Availability (Astana)** | Landsat 4-9, Sentinel-2, ERA5 weather data pre-indexed | Sentinel-1/2, Landsat on demand | Full archive, but requires local disk storage (>100 GB) |
| **Rate Limits & Academic Pricing** | Generous free non-commercial tier for academic research | Limited free requests, paid for high-volume batch | Completely free, but high local bandwidth/storage burden |
| **Integration with Python ML** | Export to NumPy / GeoPandas via earthengine-api | Native GeoTIFF/NumPy arrays | Native GDAL integration |

### Justification & Selection: **Alternative A + B Hybrid**
We select **Google Earth Engine (GEE) Python API** as the primary engine for historical catalog extraction, cloud filtering, and large-scale index compositing, complemented by **Rasterio/GeoPandas** for localized parcel rasterization. This avoids storing hundreds of gigabytes of raw multi-spectral tiles on local disks while leveraging Google's pre-computed top-of-atmosphere calibrations.

---

## 3. Decision 2: ML Model for Surface Temperature (LST) & UHI Forecasting

### Evaluated Alternatives
- **Alternative A: Gradient Boosted Decision Trees (LightGBM / XGBoost)**
- **Alternative B: Deep Convolutional Neural Networks (U-Net / CNN)**
- **Alternative C: Classical Spatial Econometrics (Spatial Lag / SAR / OLS Regression)**

### Comparison Table

| Evaluation Criteria | Alt A: LightGBM / XGBoost | Alt B: Deep Learning (U-Net) | Alt C: Spatial Lag Model (SAR) |
|---|---|---|---|
| **Non-linear Relationship Modeling** | Excellent (Captures complex vegetation-heat non-linearities) | Excellent (Learns spatial convolutions directly) | Poor (Strictly linear assumptions) |
| **Inference Latency** | Sub-second (< 50 ms for tabular feature grid) | High (1–5 s on GPU, > 10 s on CPU) | Instant (< 20 ms) |
| **Interpretability (SHAP / Feature Importance)** | High (Tree SHAP explains impact of each feature) | Low (Black-box convolutions) | High (Standard regression coefficients) |
| **Data Sample Efficiency** | Trains effectively on thousands of sampled pixels | Requires massive labeled datasets, prone to overfitting | Highly sensitive to multicollinearity |
| **Hardware Requirements** | Runs smoothly on standard CPU server | Requires dedicated GPU (CUDA) in production | Low CPU |

### Justification & Selection: **Alternative A (LightGBM / XGBoost)**
We select **LightGBM / XGBoost**. Gradient boosted trees consistently achieve state-of-the-art accuracy on tabular geospatial features (indices, distances, densities) without requiring GPU acceleration. Crucially, Tree SHAP provides interpretable explanations for city planners (e.g., *"increasing tree canopy by 20% in this parcel decreases surface temperature by $1.8^\circ\text{C}$"*), which is vital for civil decision-making.

---

## 4. Decision 3: Backend Server Platform and Spatial Data Storage

### Evaluated Alternatives
- **Alternative A: FastAPI + PostgreSQL 16 / PostGIS**
- **Alternative B: Django + GeoDjango + PostgreSQL**
- **Alternative C: Node.js (Express) + MongoDB with Geospatial 2dsphere Indices**

### Comparison Table

| Evaluation Criteria | Alt A: FastAPI + PostGIS | Alt B: Django + GeoDjango | Alt C: Express + MongoDB |
|---|---|---|---|
| **Asynchronous Performance & Latency** | Extremely high (Asynchronous ASGI, Starlette/Uvicorn) | Moderate (Synchronous WSGI default) | High (Event loop) |
| **Spatial Query Capabilities** | Industry gold standard (ST_DWithin, ST_Intersection, pgRouting) | High (PostGIS via ORM), but overhead in complex queries | Basic (Only simple point/polygon bounding boxes) |
| **Python Ecosystem Synergy** | Native Python (Direct sharing of NumPy/GeoPandas objects) | Native Python | Split stack (Node.js backend must call Python ML via subprocess/RPC) |
| **API Documentation** | Automated OpenAPI 3.0 / Swagger & ReDoc generation | Requires third-party DRF-YASG | Manual Swagger setup |
| **Memory Footprint** | Lightweight (~40 MB per worker) | Heavy (>150 MB per worker) | Lightweight |

### Justification & Selection: **Alternative A (FastAPI + PostgreSQL / PostGIS)**
We select **FastAPI with PostgreSQL / PostGIS**. PostGIS provides unmatched spatial analytical functions (topological operations, spatial buffering, indexation via R-Tree/GiST). FastAPI offers ultra-low latency, native asynchronous request handling, automatic interactive Swagger documentation, and direct integration with Python ML pipelines without inter-language overhead.
