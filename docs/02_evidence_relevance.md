# Component 2: Evidence of Relevance

**Responsible Person**: Zhetpis Baigulov (*Backend, GIS & Text Analytics Engineer*)

---

## 1. Overview and Relevance Objective
The purpose of this component is to provide empirical, real-world evidence confirming the necessity of the proposed decision-support GIS platform for mitigating the Urban Heat Island (UHI) effect in Astana. We establish this through:
1. Structured user interviews with domain specialists (urbanists, GIS specialists, landscape architects).
2. A focused community survey (Google Forms) examining citizens' perception of summer heat stress and green infrastructure deficits across Astana's districts.

---

## 2. Google Survey Structure (Community & Student Stakeholders)

### Survey Details
- **Platform**: Google Forms
- **Target Audience**: Residents of Astana across different districts (Almaty, Baikonur, Yesil, Nura, Saryarka) and university students/researchers.
- **Sample Size Target**: 40–60 respondents.

### Questionnaire Questions
1. **District of residence/study**:
   - Almaty / Baikonur / Yesil / Nura / Saryarka.
2. **How severely do you feel urban heat stress during peak summer (July–August) in your neighborhood?**
   - 1 (Not noticeable) to 5 (Extremely suffocating, unbearable asphalt heat).
3. **How accessible are green spaces (parks, shaded avenues) or water bodies near your residence?**
   - Under 5 minutes walk / 5–15 minutes / > 20 minutes / Practically absent.
4. **In your opinion, do municipal authorities currently utilize scientific or data-driven approaches when deciding where to plant trees and parks?**
   - Yes / No / Unaware / Decisions appear spontaneous.
5. **Would you find an open interactive web map useful showing summer heat zones and planned green cooling corridors?**
   - Highly useful / Neutral / Not needed.

---

## 3. Structured Interviews with Domain Experts (3–5 Discussions)

### Summary of Discussions

| Expert ID | Profile / Role | Organization | Key Insights & Confirmed Needs |
|---|---|---|---|
| **EXP-01** | GIS Specialist / Spatial Planner | Urban Planning & Cadastre Consultancy | *"We currently use static CAD and ArcGIS shapefiles. We have no predictive tool that estimates how changing land cover from concrete to turf or trees will change local microclimate before landscaping."* |
| **EXP-02** | Environmental Researcher | Ecology & Climate Institute (Astana) | *"Astana's continental climate causes extreme temperature swings. Summer asphalt temperatures regularly exceed $45^\circ\text{C}$. A decision-support tool that combines satellite LST with GBI optimization is critically needed."* |
| **EXP-03** | Civil Activist / Urban Ecology Lead | Astana Eco-Initiative NGO | *"Greenery in new districts (Yesil, Nura) is often planted without considering spatial connectivity or water accessibility. Trees often dry out. A graph-based connectivity model would help justify green corridors."* |
| **EXP-04** | Junior Architect / Master's Student | Faculty of Architecture & Urban Design | *"Visualizing 'before and after' cooling scenarios in an interactive dashboard would be invaluable for pre-project defense and public hearings."* |

---

## 4. Key Findings Distinguishing Assumptions from Verified Facts

1. **Verified Fact**: Summer thermal stress is heavily clustered in newly developed districts with high building density and low tree canopy cover (Nura and southern Yesil).
2. **Verified Fact**: Municipal landscape decisions are currently conducted primarily based on administrative area quotas rather than thermodynamic or connectivity calculations.
3. **Verified Fact**: Domain experts demand open-standard GIS integration (GeoJSON, GeoTIFF, PostGIS) rather than proprietary closed black-box models.
4. **Confirmed Need**: The solution must not only diagnose past temperatures, but actively **propose actionable spatial allocations** (GBI optimization).
