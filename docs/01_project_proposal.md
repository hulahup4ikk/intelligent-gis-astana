# Component 1: Project Proposal

## 1. Project Title
**Development of an Intelligent Geographic Information System for Graph-Based Analysis, Forecasting, and Optimization of Green-Blue Infrastructure to Mitigate the Urban Heat Island Effect in Astana**


---

## 2. Team Members and Supervisor
- **Ivan Kuznetsov** (Student ID: 241258, Group SE-2417): *Machine Learning & Spatial Data Science Engineer, Project Lead (Git & YouTrack)*
- **Zhetpis Baigulov** (Student ID: 242181, Group SE-2417): *Backend, GIS & Text Analytics Engineer*
- **Arstan Kutzhanovich Makatov**: *Academic Supervisor, Senior Lecturer, School of Software Engineering, Astana IT University*

---

## 3. Problem Statement
The city of Astana experiences rapid urbanization, marked by extensive construction of multi-story residential districts, expansion of asphalt and concrete road networks, and substantial reduction of natural land cover. These conditions generate a severe **Urban Heat Island (UHI)** effect during summer months, leading to:
- Surface temperatures in dense built-up areas exceeding peripheral rural areas by $4^\circ\text{C}$ to $9^\circ\text{C}$.
- Heightened thermal discomfort and cardiovascular health hazards for citizens.
- Increased energy consumption for air conditioning.
- Accelerated ecological degradation due to isolated, fragmented urban green spaces.

Current municipal planning in Astana lacks automated, data-driven decision support tools that simulate how new parks, water bodies, or tree corridors (Green-Blue Infrastructure — GBI) will affect microclimate and surface temperatures before construction begins.

---

## 4. Target Users
1. **Astana Urban Planning & Land Management Authorities**: specialists responsible for master plan zoning, green space quotas, and district renovation.
2. **Department of Ecology and Environment of Astana**: environmental auditors monitoring thermal anomalies and vegetation health.
3. **Landscape Architects and Urban Planners**: practitioners designing localized public spaces, parks, and boulevards.
4. **City Researchers and Citizens**: open data advocates and eco-initiatives interested in microclimate and air comfort.

---

## 5. Aim and Objectives

### Aim
To design and develop an intelligent geographic information platform capable of ingesting multi-spectral satellite imagery, modeling urban thermal dynamics using machine learning, assessing ecological connectivity via graph theory, and generating optimized spatial allocations for green-blue infrastructure to mitigate the Urban Heat Island effect in Astana.

### Objectives
1. **Data Pipeline**: Build an automated data ingestion pipeline for multi-spectral satellite imagery (Landsat 8/9, Sentinel-2) and compute key remote sensing indices (LST, NDVI, NDWI, NDBI).
2. **Predictive Modeling**: Train and validate supervised machine learning models (Gradient Boosting / Random Forest) to predict Land Surface Temperature (LST) based on urban density, vegetation, and surface properties.
3. **Graph-Based Spatial Modeling**: Model Astana's green and blue network as a spatial graph to compute ecological connectivity and accessibility metrics.
4. **Optimization Engine**: Implement a multi-objective heuristic/genetic optimization algorithm (e.g., NSGA-II) to recommend optimal spatial configurations for new green-blue interventions under spatial and budgetary constraints.
5. **System Integration & Web UI**: Implement a cloud-ready backend (FastAPI, PostgreSQL/PostGIS) and an interactive web dashboard (React, Mapbox GL) to visualize heat maps and simulation scenarios.
6. **Empirical Evaluation**: Benchmark model accuracy against historical satellite recordings and validate usability with domain stakeholders.

---

## 6. Expected Outcomes
- An end-to-end data pipeline processing Earth observation rasters into analytical GIS layers.
- An ML regression model achieving $R^2 \ge 0.75$ and $\text{RMSE} \le 1.8^\circ\text{C}$ in surface temperature forecasting.
- A functional decision-support web application providing scenario-based "what-if" planning for municipal officers.
- Reproducible open-source repository with automated testing, CI/CD, and documented API endpoints.

---

## 7. Project Scope

### In Scope
- Geographical boundary: Astana city urbanized area and immediate suburban green belt.
- Temporal satellite imagery: Multi-spectral summer scenes (June–August, 2019–2026) with cloud cover $< 10\%$.
- Remote sensing indices: LST (Land Surface Temperature), NDVI (Vegetation), NDWI (Water), NDBI (Built-up).
- Predictive models: XGBoost, LightGBM, Random Forest, Spatial Regression.
- Web dashboard with interactive layers and scenario simulation.

### Out of Scope
- 3D computational fluid dynamics (CFD) wind-tunnel simulations (e.g., building-level turbulence).
- Real-time IoT sensor network deployment across city streets (satellite-driven and open meteo station data used instead).
- Autonomous legal issuance of construction permits (system provides advisory recommendations only).
