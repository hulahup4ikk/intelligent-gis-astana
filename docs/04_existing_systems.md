# Component 4: Existing System Comparison

**Responsible Person**: Zhetpis Baigulov (*Backend, GIS & Text Analytics Engineer*)

---

## 1. Objective and Systems Selection
To justify the necessity of developing an intelligent GIS platform for Astana, we benchmarked four leading existing systems and software packages currently used in urban microclimate modeling and green infrastructure assessment:

1. **InVEST Urban Cooling Model** (Stanford University Natural Capital Project): Widely adopted open-source ecosystem services tool for calculating heat mitigation based on shading and evapotranspiration.
2. **ENVI-met**: Industry-standard 3D non-hydrostatic computational fluid dynamics (CFD) microclimate simulation software.
3. **QGIS with LST / UHI Processing Plugins** (e.g., Semi-Automatic Classification Plugin / SCP): Desktop GIS extension for calculating surface temperatures from satellite bands.
4. **Google Environmental Insights Explorer (EIE) / Tree Canopy Lab**: Cloud-based web portal for inspecting urban tree canopy and heat vulnerability.

---

## 2. Comparison Criteria (8 Key Metrics)

1. **Spatial Scale Coverage**: Ability to seamlessly analyze the entire metropolitan area ($>800\text{ km}^2$) down to district parcels.
2. **Automated Multi-Spectral Satellite Ingestion**: Direct cloud API integration for regular time-series updates without manual file downloads.
3. **Real-time "What-If" Scenario Simulation**: Sub-second feedback when an urban planner modifies land cover or adds green patches.
4. **Graph-Based Ecological Connectivity Modeling**: Evaluation of green-blue corridors and ecological networks using graph theory.
5. **Algorithmic Spatial Optimization**: Automated search (e.g., genetic algorithms) to recommend best locations for new interventions.
6. **Web-Based Interactive Accessibility**: Cloud-hosted browser interface without requiring specialized local GIS or desktop software.
7. **Computational Speed**: Execution turnaround time for city-wide simulation.
8. **Adaptability to Local Climate (Astana Steppe Zone)**: Support for extreme continental temperature swings and custom local cadastre data.

---

## 3. Comparison Matrix

| Criteria | InVEST Urban Cooling Model | ENVI-met | QGIS (SCP / Thermal Plugins) | Google EIE / Tree Canopy | **Proposed System (Our Solution)** |
|---|---|---|---|---|---|
| **1. Spatial Scale** | Meso-scale (City/Subbasin) | Micro-scale ($100\text{ m} \times 100\text{ m}$ to $1\text{ km}^2$) | Any raster resolution | City/District boundaries | **Multi-scale (City-wide down to parcel level)** |
| **2. Satellite Ingestion** | Manual (Requires pre-processed GeoTIFF inputs) | None (Requires 3D geometry building models) | Semi-automated (Manual download / plugin search) | Automated (Google proprietary data) | **Automated (Direct API integration with Sentinel Hub / GEE)** |
| **3. "What-If" Simulation** | Batch processing (minutes to hours per run) | Very slow (Hours to days of CFD calculation) | None (Static analytical raster calculation) | Read-only inspection (No custom scenario editing) | **Real-Time Interactive (< 2 seconds via trained ML surrogate model)** |
| **4. Graph Connectivity** | No (Treats green patches independently) | No (Focuses on 3D physics / wind) | Manual (Requires complex plugin workflows) | No | **Yes (Native NetworkX graph engine for ecological corridors)** |
| **5. Algorithmic Optimization** | No (Manual trial-and-error by user) | No | No | No | **Yes (Multi-objective Genetic Algorithm NSGA-II for parcel allocation)** |
| **6. Web-based Accessibility** | No (Standalone desktop Python tool) | No (Heavy desktop Windows software) | No (Desktop C++/Python software) | Yes (Web portal) | **Yes (Cloud FastAPI + React + Mapbox GL interactive web dashboard)** |
| **7. Computation Time** | 5–30 minutes per city run | 6–48 hours per simulation | 10–20 minutes | Instant (Pre-computed tiles) | **Sub-second for cached layers, < 3s for ML prediction** |
| **8. Local Climate & Cadastre** | Generic empirical equations | Physical equations, but hard to calibrate | Generic raster math | Fixed metrics, closed model for Astana | **Calibrated on Astana Landsat/Sentinel history & local cadastre** |

---

## 4. Evidence-Based Justification of the Proposed System

The comparison matrix demonstrates an evident market gap:
- **Physics-heavy micro tools (ENVI-met)** provide high 3D accuracy but are computationally prohibitive for city-wide master planning and cannot run dynamic optimization.
- **Desktop GIS tools (QGIS, InVEST)** are static, difficult for municipal decision-makers without GIS engineering backgrounds to operate, and lack automated optimization algorithms.
- **Commercial web tools (Google EIE)** provide read-only visualizations without allowing planners to test custom planning interventions or access open raw calculation layers.

**Conclusion**: The proposed platform fulfills an urgent need for an **interactive, web-based, AI-powered decision support system** combining the macro-scale coverage of satellite remote sensing with the predictive speed of machine learning and the prescriptive power of graph-based spatial optimization.
