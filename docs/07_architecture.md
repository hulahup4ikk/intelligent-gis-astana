# Component 7: Architecture and Diagrams

**Responsible Persons**: 
- System Context & Use Case Diagrams: Zhetpis Baigulov
- ML Component & Data Pipeline Diagram: Ivan Kuznetsov

---

## 1. Architectural Overview
The system follows a modular, cloud-ready architecture designed to support heavy spatial data processing, machine learning inference, and responsive web visualization. The architecture aligns with the C4 model standards, encompassing:
1. **System Context (Level 1)**: Interactions between urban planners, external satellite APIs, and the core platform.
2. **Use Case Modeling**: User interactions, simulation workflows, and administrative actions.
3. **Component & Data Flow Diagram (Level 3 - Draft)**: Internal structure connecting satellite ingestion, GeoPandas/Rasterio preprocessing, LightGBM/XGBoost inference, PostGIS storage, and the FastAPI application layer.

Editable source files for all diagrams are preserved in the [`diagrams/`](../diagrams/) directory in `.drawio` format.

---

## 2. System Context Diagram (C4 Level 1)

```mermaid
flowchart TD
    User["👤 Urban Planner / Municipal Auditor"]
    EcoUser["👤 Environmental Researcher / Citizen"]
    
    subgraph GBI_SYSTEM ["Intelligent GBI & UHI Decision Support Platform"]
        WebUI["Web GIS Dashboard (React + Mapbox GL)"]
        APIGateway["Backend REST API (FastAPI)"]
        SpatialDB["Spatial Database (PostgreSQL 16 + PostGIS)"]
        MLEngine["ML & Optimization Engine (Python, LightGBM, DEAP)"]
        
        WebUI <-->|HTTPS / JSON / GeoJSON| APIGateway
        APIGateway <-->|SQL / Spatial Queries| SpatialDB
        APIGateway <-->|RPC / Job Queue| MLEngine
        MLEngine <-->|Vector/Raster read/write| SpatialDB
    end
    
    subgraph EXTERNAL ["External Data Providers"]
        GEE["Google Earth Engine API / Sentinel Hub"]
        OSM["OpenStreetMap / Astana Cadastre"]
        Meteo["Open-Meteo Weather API"]
    end
    
    User -->|Simulates GBI scenarios & inspects heatmaps| WebUI
    EcoUser -->|Views historical thermal trends & public data| WebUI
    MLEngine -->|Fetches satellite scenes & thermal bands| GEE
    MLEngine -->|Extracts urban road/building vectors| OSM
    MLEngine -->|Retrieves ambient summer temperatures| Meteo
```

---

## 3. Use Case Diagram

```mermaid
flowchart LR
    Planner["👤 Urban Planner / Municipal Specialist"]
    Admin["👤 System Administrator"]
    
    subgraph UC ["System Use Cases"]
        UC1(["UC-01: Inspect City Thermal Maps & Hotspots"])
        UC2(["UC-02: Query Neighborhood Microclimate & Vegetation Index"])
        UC3(["UC-03: Simulate Custom GBI Scenario (What-If)"])
        UC4(["UC-04: Run Automated Multi-Objective Optimization"])
        UC5(["UC-05: Export Spatial Layers (GeoJSON / PDF Report)"])
        UC6(["UC-06: Trigger Satellite Data Ingestion Pipeline"])
        UC7(["UC-07: Retrain & Benchmark ML Prediction Model"])
    end
    
    Planner --> UC1
    Planner --> UC2
    Planner --> UC3
    Planner --> UC4
    Planner --> UC5
    
    Admin --> UC6
    Admin --> UC7
```

---

## 4. Component Diagram (Draft) and Data Flow

```mermaid
flowchart TD
    subgraph INGESTION ["1. Data Ingestion & Preprocessing Subsystem"]
        S1["Sentinel-2 & Landsat 8/9 Rasters"] --> P1["Cloud Filtering & Radiometric Calibration"]
        P1 --> P2["Index Calculation (NDVI, NDWI, NDBI, LST)"]
        P2 --> P3["Spatial Resampling (30m Grid) & Cadastre Masking"]
    end
    
    subgraph STORAGE ["2. Storage Subsystem"]
        P3 --> GeoDB[("PostgreSQL / PostGIS\n- Spatial Layers\n- Parcel Geometries\n- Historical LST")]
        P3 --> RasterStore[("Cloud / Local Raster Store\n- Cloud Optimized GeoTIFFs (COG)")]
    end
    
    subgraph ANALYTICS ["3. Intelligence & Analytics Engine"]
        GeoDB --> FeatEng["Spatial Feature Extraction\n(Building density, Distance to water, Tree cover)"]
        FeatEng --> MLModel["Surrogate ML Predictor\n(LightGBM / XGBoost Regressor)"]
        GeoDB --> GraphMod["Graph Connectivity Module\n(NetworkX Urban Eco-Graph)"]
        
        MLModel --> OptEngine["Multi-Objective Optimization Engine\n(NSGA-II Genetic Algorithm)"]
        GraphMod --> OptEngine
    end
    
    subgraph SERVING ["4. Serving & Presentation Subsystem"]
        OptEngine --> FastAPISvc["FastAPI Application Server"]
        RasterStore --> TileServer["Vector/Raster Tile Server"]
        FastAPISvc <--> WebClient["React Frontend (Mapbox GL JS / Leaflet)"]
        TileServer --> WebClient
    end
```

---

## 5. Architectural Alignment Matrix
- **Requirements to Architecture**:
  - `FR-01, FR-02` $\rightarrow$ Ingestion Subsystem (`src/ml/indices.py`).
  - `FR-03, FR-04` $\rightarrow$ Serving Subsystem (`src/backend/main.py`) & ML Engine.
  - `FR-05, FR-06` $\rightarrow$ Graph Network & Optimization Engine.
  - `FR-07` $\rightarrow$ React + Mapbox GL Dashboard.
