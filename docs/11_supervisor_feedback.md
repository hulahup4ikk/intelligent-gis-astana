# Component 11: Supervisor Feedback Protocol (Pre-Defense 1)

**Academic Supervisor**: Arstan Kutzhanovich Makatov  
*Senior Lecturer, School of Software Engineering, Astana IT University*  
**Diploma Project**: Development of an Intelligent GIS for Graph-Based Analysis, Forecasting, and Optimization of Green-Blue Infrastructure to Mitigate the Urban Heat Island Effect in Astana  
**Review Date**: 24 October 2026  

---

## 1. General Evaluation of Pre-Defense 1 Readiness
The project materials presented by the team for Pre-Defense 1 demonstrate a high degree of maturity, scientific rigor, and adherence to Software Engineering standards. The problem formulation regarding Astana's urban heat island effect is well-grounded in empirical research and multi-spectral satellite remote sensing principles. Project management via YouTrack (14 verified tickets) and continuous Git version control with peer-reviewed Pull Requests meet all departmental criteria.

---

## 2. Evaluation by Area of Responsibility

### Part 1: Machine Learning & Spatial Data Science Pipeline (Ivan Kuznetsov)
* **Feedback on Deliverables**:
  - The critical literature review is comprehensive, covering 12+ authoritative sources with a clear identification of research gaps in localized urban microclimatic modeling.
  - The decision to reject standard random cross-validation in favor of **Spatial Block K-Fold Cross-Validation** (with 5 km buffers) is mathematically sound and essential for preventing spatial autocorrelation bias (Tobler's First Law).
  - The mathematical implementation of remote sensing indices (`NDVI`, `NDWI`, `NDBI`, and `LST`) in `src/spatial_indices.py` demonstrates solid proficiency in vectorized computing, confirmed by automated unit tests.
* **Recommendations for Subsequent Stages**:
  - In Milestone 2, ensure satellite raster normalization accommodates seasonal variance across summer multi-temporal composites.
  - Proceed with baseline model training (LightGBM/XGBoost) comparing thermal predictions against ground meteorological station measurements.

---

### Part 2: Backend, Spatial Database & User Experience (Zhetpis Baigulov)
* **Feedback on Deliverables**:
  - The stakeholder relevance survey with 30 verified respondents across Astana provides strong empirical justification for the project, directly linking user pains to functional requirements.
  - The comparative benchmark of existing systems (InVEST, ENVI-met, QGIS) clearly highlights the unique value proposition of automated optimization over manual scenario simulation.
  - The architectural documentation (C4 Context and UML Use Case diagrams) and initial FastAPI schema prototypes provide a clean foundation for the backend microservice.
* **Recommendations for Subsequent Stages**:
  - For Milestone 2, implement PostGIS spatial R-Tree (GiST) indexing early to guarantee sub-second polygon queries during multi-user web dashboard sessions.
  - Finalize API endpoints for vector GeoJSON ingestion and scenario export.

---

## 3. Pre-Defense 1 Conclusion
Both students have fulfilled their individual milestone obligations in full. The separation of duties between machine learning data pipelines (Ivan) and backend spatial infrastructure/UI (Zhetpis) is well-balanced. 

**Decision**: The project is approved and recommended for presentation at Pre-Defense 1.
