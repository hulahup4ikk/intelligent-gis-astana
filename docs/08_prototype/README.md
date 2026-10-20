# Component 8: UX Scenarios and Prototype Specification

**Responsible Person**: Zhetpis Baigulov (*Backend, GIS & Text Analytics Engineer*)

---

## 1. Prototype Overview
The prototype provides both interactive visual interactions (via UI mockups in Figma) and verifiable programmatic interactions (via the running FastAPI REST API). It demonstrates how urban planners and environmental specialists interact with the system to diagnose heat anomalies and optimize green-blue interventions.

---

## 2. Key User Scenarios

### Scenario 1: City-Wide Thermal Heat Island Inspection
- **User Action**: Urban planner opens the web dashboard, selects the summer observation period (e.g., July 2026), and enables the *Land Surface Temperature (LST)* heatmap overlay.
- **System Response**: Interactive map displays a color-coded raster gradient (from blue $22^\circ\text{C}$ to deep red $42^\circ\text{C}$). Clicking on any district (e.g., Nura District) displays the local average temperature, NDVI vegetation fraction, and comparison with city-wide baseline.

### Scenario 2: Interactive "What-If" Land Cover Modification
- **User Action**: The planner selects a 4-hectare barren or asphalt lot in an identified thermal hotspot and tests converting 60% of the surface into an urban park with a cooling retention pond.
- **System Response**: Frontend sends the polygon geometry and modified surface attributes to `POST /api/v1/forecast`. Within 1.5 seconds, the map dynamically renders the projected thermal reduction (e.g., $\Delta T = -2.4^\circ\text{C}$) and updates the local comfort score.

### Scenario 3: Algorithmic GBI Allocation under Budget Constraints
- **User Action**: The planner specifies a district boundary (e.g., Yesil District), sets a spatial intervention budget (e.g., $50,000\text{ m}^2$ of new greenery/water), and clicks *"Run Multi-Objective Optimization"*.
- **System Response**: The NSGA-II optimization engine iterates across candidate vacant municipal parcels and returns the top-3 Pareto-optimal spatial configurations balancing maximum cooling vs. maximum ecological network connectivity.

---

## 3. Web Dashboard Mockup Wireframe Layout (Figma Blueprint)

```text
+----------------------------------------------------------------------------------------------------+
|  [Logo] GBI-UHI Intelligence Platform — Astana                          [District: Yesil]  [User]  |
+------------------------------------+---------------------------------------------------------------+
|  CONTROLS & SCENARIO BUILDER       |  INTERACTIVE MAPBOX GL CANVAS                                 |
|                                    |                                                               |
|  [✓] Thermal Layer (LST 2026)      |    [ Map View: Center Astana (51.1694 N, 71.4491 E) ]         |
|  [✓] Vegetation Index (NDVI)       |                                                               |
|  [ ] Water Corridors (NDWI)        |            ( Hotspot: Industrial / Nura )                     |
|  [✓] Cadastral Parcels             |                 [🔴 38.6°C Asphalt Area]                      |
|                                    |                                                               |
|  --- Scenario Parameters ---       |                 [🟢 Planned Green Corridor]                   |
|  Green Intervention: [ 45,000 m² ] |                       \                                       |
|  Water Body Ratio:   [ 20%      ]  |                        \--- Cooling effect: -2.3°C            |
|                                    |                                                               |
|  [ Run AI Simulation ]             |                                                               |
|  [ Run Multi-Obj Optimization ]    |                                                               |
+------------------------------------+---------------------------------------------------------------+
|  METRICS & ANALYTICS BAR:                                                                          |
|  Current Mean Temp: 31.8°C | Projected Temp: 29.5°C (-2.3°C) | Connectivity Index: +18.4% | Budget: OK |
+----------------------------------------------------------------------------------------------------+
```

---

## 4. API Prototype Contract (Input & Output Specifications)

### Endpoint 1: Query Layer Catalog
- **Method**: `GET /api/v1/layers`
- **Output Sample**:
```json
[
  {
    "layer_id": "uhi_lst_astana",
    "name": "Land Surface Temperature (LST)",
    "type": "raster",
    "description": "Calculated surface temperature layer derived from Landsat 8/9 TIRS band",
    "last_updated": "2026-07-15"
  }
]
```

### Endpoint 2: What-If Thermal Forecast
- **Method**: `POST /api/v1/forecast`
- **Input Payload**:
```json
{
  "bounds": [71.38, 51.12, 71.46, 51.18],
  "resolution_meters": 30,
  "date_range": "2026-07-01_2026-08-31"
}
```
- **Output Sample**:
```json
{
  "status": "simulated",
  "bounds": [71.38, 51.12, 71.46, 51.18],
  "resolution": 30,
  "mean_projected_lst_celsius": 32.4,
  "uhi_intensity_hotspots_detected": 4,
  "message": "Spatial forecast calculated successfully using trained gradient boosting model"
}
```

### Endpoint 3: Multi-Objective GBI Optimization
- **Method**: `POST /api/v1/optimize`
- **Input Payload**:
```json
{
  "target_area_id": "DISTRICT-YESIL-04",
  "budget_sq_meters": 50000.0,
  "infrastructure_type": "mixed_green_blue"
}
```
- **Output Sample**:
```json
{
  "status": "optimized",
  "target_area_id": "DISTRICT-YESIL-04",
  "allocated_sq_meters": 50000.0,
  "infrastructure_type": "mixed_green_blue",
  "estimated_lst_reduction_celsius": 2.1,
  "suggested_parcels": [
    {"parcel_id": "AST-URB-104", "type": "park_zone", "priority": 1},
    {"parcel_id": "AST-URB-219", "type": "cooling_pond", "priority": 2}
  ]
}
```
