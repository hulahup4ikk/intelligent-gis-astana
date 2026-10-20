# System Architecture and Design Diagrams

This directory contains the editable source files and exports for all architectural and design diagrams required for the diploma pre-defense.

## Files

1. **System Context Diagram (C4 Level 1)**
   - Source: `system_context.drawio`
   - Description: Illustrates high-level boundaries, domain actors (Urban Planners, Environmental Researchers), external satellite APIs (GEE, Sentinel Hub, OpenStreetMap), and the core GBI-UHI decision support platform.

2. **UML Use Case Diagram**
   - Source: `use_case.drawio`
   - Description: Details planner and administrator interaction scenarios, including heatmap inspection, what-if simulation, and multi-objective GBI optimization.

3. **ML Component & Data Pipeline Diagram**
   - Source: `ml_pipeline.drawio`
   - Description: Maps the end-to-end data flow from raw Sentinel/Landsat rasters, through cloud masking, index calculation (NDVI/LST), feature extraction, surrogate ML prediction (LightGBM), to spatial PostGIS storage and FastAPI delivery.

## How to View and Edit
- Open [draw.io (diagrams.net)](https://app.diagrams.net/) in your web browser.
- Select **Open Existing Diagram** and pick any `.drawio` file from this folder.
- Alternatively, install the **Draw.io Integration** extension in VS Code.

---

## Diagram Previews (Mermaid)

The diagrams below are Mermaid replicas of the `.drawio` source files, rendered natively by GitHub for quick reading.

### 1. System Context Diagram (C4 Level 1)

```mermaid
graph LR
    UP["🧑‍💼 Urban Planner /<br/>Municipal Specialist"]
    ER["🔬 Environmental<br/>Researcher"]

    subgraph Platform["GBI & UHI Decision Support Platform"]
        direction TB
        API["FastAPI Backend"]
        DB["PostGIS Database"]
        ML["ML Engine"]
        UI["React Web Dashboard"]
    end

    SAT["🛰️ Satellite APIs<br/>(GEE / Sentinel Hub)"]
    OSM["🗺️ OpenStreetMap &<br/>Astana Cadastre"]

    UP -- "Simulates scenarios &<br/>inspects heatmaps" --> Platform
    ER -- "Queries climate indices &<br/>analyzes GBI connectivity" --> Platform
    Platform -- "Queries multi-spectral<br/>tiles & LST" --> SAT
    Platform -- "Extracts parcels<br/>& road network" --> OSM
```

### 2. UML Use Case Diagram

```mermaid
graph LR
    Planner["🧑‍💼 Urban Planner"]
    Admin["⚙️ System Admin"]

    subgraph System["GBI-UHI Intelligence Platform"]
        UC1["UC-01: Inspect City<br/>Thermal Maps & Hotspots"]
        UC2["UC-02: Query Local<br/>Microclimate Indices"]
        UC3["UC-03: Simulate What-If<br/>Land Cover Scenario"]
        UC4["UC-04: Run Multi-Objective<br/>GBI Optimization"]
        UC5["UC-05: Trigger Satellite<br/>Data Pipeline"]
        UC6["UC-06: Retrain &<br/>Benchmark ML Model"]
    end

    Planner --> UC1
    Planner --> UC2
    Planner --> UC3
    Planner --> UC4
    Admin --> UC5
    Admin --> UC6
```

### 3. ML & Data Pipeline Diagram

```mermaid
graph LR
    P1["1. Sentinel-2 &<br/>Landsat 8/9 Rasters"]
    P2["2. Cloud Masking &<br/>Calibration<br/>(QA Pixel, Split-Window LST)"]
    P3["3. Index Calculation<br/>(NDVI, NDWI, NDBI)"]
    P4[("4. Spatial Feature Store<br/>(PostGIS + R-Tree Grids)")]
    P5["5. Surrogate Regressor<br/>(LightGBM / XGBoost)"]
    P6["6. NSGA-II<br/>Multi-Objective Optimizer"]
    P7["7. FastAPI Serving &<br/>Web Map UI"]

    P1 --> P2 --> P3 --> P4 --> P5 --> P6 --> P7
```
