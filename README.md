# Development of an Intelligent Geographic Information System for Graph-Based Analysis, Forecasting, and Optimization of Green-Blue Infrastructure to Mitigate the Urban Heat Island Effect in Astana

[![Status: Pre-Defense 1](https://img.shields.io/badge/Status-Pre--Defense%201%20(Ready)-orange)]()
[![Python: 3.11+](https://img.shields.io/badge/Python-3.11+-blue)]()
[![License: Academic](https://img.shields.io/badge/License-Academic%20Diploma-green)]()

## 1. Project Title and Brief Description
**Development of an Intelligent Geographic Information System for Graph-Based Analysis, Forecasting, and Optimization of Green-Blue Infrastructure to Mitigate the Urban Heat Island Effect in Astana.**

This project is a software-analytical decision support system (DSS) combining Earth Observation (EO) remote sensing, spatial data science, machine learning, and spatial graph optimization. It identifies localized microclimatic thermal discomfort zones (Urban Heat Island — UHI) across the city of Astana and algorithmically generates science-backed planning scenarios for allocating urban green spaces and water retention corridors (Green-Blue Infrastructure — GBI).

---

## 2. Problem Statement, Target Users, and Expected Outcomes

### Problem Statement
The city of Astana faces severe summer Urban Heat Island (UHI) phenomena driven by rapid urban expansion, high ratios of impervious surface materials (asphalt, concrete), dense multi-story residential blocks, and fragmented existing vegetation. Current municipal urban planning and landscape interventions are implemented without continuous multi-spectral satellite thermal monitoring or predictive mathematical modeling of the thermodynamic cooling capacity of green-blue infrastructure.

### Target Users
1. **Astana Urban Planning & Land Management Authorities**: Municipal specialists responsible for master plan zoning, green space quotas, and district renovation.
2. **Department of Ecology and Environment of Astana**: Environmental auditors monitoring microclimatic risks, surface temperature anomalies, and urban vegetation health.
3. **Urban Planners, Landscape Architects, and Research Centers**: Practitioners modeling localized microclimatic scenarios and evaluating ecological corridor connectivity.

### Expected Outcomes
- An automated ingestion and preprocessing pipeline for multi-spectral satellite imagery (Sentinel-2, Landsat 8/9) with calculation of key remote sensing indices (LST, NDVI, NDWI, NDBI).
- A machine learning regression surrogate model forecasting Land Surface Temperature (LST) with accuracy $R^2 \ge 0.75$ and $\text{RMSE} \le 1.8^\circ\text{C}$.
- A spatial graph model assessing the ecological and physical connectivity of the city's green-blue infrastructure.
- A multi-objective optimization engine (NSGA-II) algorithmically prioritizing optimal spatial locations for new green spaces and water bodies under land and budgetary constraints.
- An interactive cloud-ready web dashboard (React, Mapbox GL / Leaflet, FastAPI) for spatial thermal visualization and dynamic "what-if" planning simulations.

---

## 3. Team Members, Responsibilities, and Supervisor

| Role | Name | Contact | Primary Areas of Responsibility |
|---|---|---|---|
| **Machine Learning & Spatial Data Science Engineer** | **Ivan Kuznetsov** | `241258@astanait.edu.kz` | Satellite remote sensing pipeline (Sentinel/Landsat), LST/NDVI/NDWI spectral indices, ML predictive modeling & spatial cross-validation, GBI optimization algorithms, Git & YouTrack lead |
| **Backend, GIS & Text Analytics Engineer** | **Zhetpis Baigulov** | `242181@astanait.edu.kz` | PostgreSQL/PostGIS spatial database architecture, graph ecological connectivity module, server-side REST API (FastAPI), web dashboard interface, stakeholder survey & UX scenarios |
| **Academic Supervisor** | **Arstan Kutzhanovich Makatov** | Senior Lecturer, School of Software Engineering, Astana IT University | General academic supervision, validation of scientific methodology and architectural decisions, stage milestone reviews |

---

## 4. Project Scope and Current Development Status

- **Current Stage**: **Pre-defense 1 (24 October 2026)**.
- **Milestone Checklist**:
  - [x] Project Proposal, Scope, and Passport definition.
  - [x] Problem relevance evidence and user research methodology.
  - [x] Critical literature review ($\ge 12$ sources, $\ge 8$ peer-reviewed journal papers).
  - [x] Benchmark comparison of existing GIS & climatic systems (InVEST, ENVI-met, QGIS, Google EIE).
  - [x] Technology stack analysis and architectural trade-off evaluations.
  - [x] Functional (FR) and non-functional (NFR) requirements specification (MoSCoW).
  - [x] System architecture design (C4 System Context, UML Use Case, ML Data Flow pipeline).
  - [x] Interactive UX wireframe mockups and FastAPI REST API prototype skeleton.
  - [x] Scientific verification and spatial cross-validation evaluation plan.
  - [x] Project management configured in YouTrack (DIP project) and Git repository structure established.

---

## 5. Selected Technologies

- **Remote Sensing & Spatial Data Pipeline**: Python 3.11+, Google Earth Engine API, Sentinel Hub API, GeoPandas, Rasterio, Shapely, NumPy.
- **Machine Learning & Optimization**: Scikit-Learn, LightGBM, XGBoost, PyGAD / DEAP (NSGA-II Genetic Algorithm).
- **Graph Network Analysis**: NetworkX, OSMnx.
- **Backend & Spatial Database**: FastAPI, PostgreSQL 16 + PostGIS, SQLAlchemy, Pydantic.
- **Frontend & GIS Visualization**: React, TypeScript, Mapbox GL JS / Leaflet, Tailwind CSS.
- **Infrastructure & Quality Assurance**: Docker, GitHub Actions, Pytest, YouTrack.

---

## 6. Project Documentation & Management Links

All mandatory documentation artifacts for Pre-Defense 1 are maintained in the [`docs/`](docs/) directory:

1. [01. Project Proposal](docs/01_project_proposal.md)
2. [02. Evidence of Relevance & User Survey](docs/02_evidence_relevance.md)
3. [03. Literature Review](docs/03_literature_review.md)
4. [04. Existing Systems Comparison](docs/04_existing_systems.md)
5. [05. Technology Comparison](docs/05_technology_comparison.md)
6. [06. Requirements Specification (SRS)](docs/06_requirements.md)
7. [07. Architecture and Diagrams](docs/07_architecture.md)
8. [08. UX Scenarios and Prototype](docs/08_prototype/README.md)
9. [09. Verification and Evaluation Plan](docs/09_verification_plan.md)
10. [10. Project Management, Risks, and Git Protocol](docs/10_risks_and_management.md)
11. [11. Supervisor Feedback](docs/11_supervisor_feedback.md)

- **YouTrack Project**: [DIP: GBI-UHI Astana](https://gbi-uhi-astana.youtrack.cloud/projects/DIP) *(Tasks DIP-01 ... DIP-14)*
- **Wireframes & Prototype**: See [docs/08_prototype/](docs/08_prototype/) *(UX scenarios and dashboard wireframe layouts)*
- **Diagram Sources & Previews**: See [diagrams/README.md](diagrams/README.md) *(Native Mermaid previews and editable `.drawio` source files)*

---

## 7. Setup, Execution, and Testing Instructions

### Prerequisites
- Python 3.11+
- Git

### Dependency Installation
```bash
# Clone the repository
git clone https://github.com/hulahup4ikk/intelligent-gis-astana.git
cd intelligent-gis-astana

# Create and activate a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Running the API Prototype
```bash
uvicorn src.backend.main:app --reload --port 8000
```
Interactive Swagger UI documentation is available at: `http://localhost:8000/docs`

### Running the Automated Test Suite
```bash
pytest tests/
# or using standard library:
python -m unittest discover tests/
```
