# Component 11: Supervisor Feedback and Iterative Improvements

**Supervisor**: Arstan Kutzhanovich Makatov (*Senior Lecturer, School of Software Engineering, Astana IT University*)  
**Team Members**: Ivan Kuznetsov, Zhetpis Baigulov

---

## 1. Supervisor Consultation Protocol

### Meeting Schedule & Cadence
- **Day & Time**: Every Wednesday, 15:00–16:00
- **Location / Format**: Astana IT University, Department consultation room / Google Meet
- **Agenda**: Sprint progress review, technical architecture critique, alignment with AITU diploma standards.

---

## 2. Feedback Log and Remediation Actions (Milestone: Pre-Defense 1)

| Session Date | Supervisor Feedback & Observations | Remediation & Decisions Made by Team | Status |
|---|---|---|---|
| **13 October 2026** | Initial review of project justifications: *“Ensure clear separation of technical duties between team members so the committee sees both students' individual contributions clearly.”* | Established strict role definition: Ivan leads ML & Data Science pipeline, Zhetpis leads Backend, PostGIS, and Web UI. Documented in `README.md` and both justification documents. | **Resolved** |
| **18 October 2026** | Methodology guidance: *“Do not rely solely on simple linear regression for LST. The urban microclimate is non-linear. Also ensure you justify why deep learning is not strictly necessary for this scale.”* | Added detailed model comparison in `docs/05_technology_comparison.md` comparing XGBoost/LightGBM vs U-Net vs Spatial Lag. Selected gradient boosting with Tree SHAP for explainability. | **Resolved** |
| **21 October 2026** | Pre-defense readiness check: *“For the 24 October submission, the committee will inspect traceability between YouTrack tickets, git branches, and PR approvals. Make sure your repository reflects continuous development rather than a single bulk commit.”* | Configured YouTrack board with DIP-01..14 tickets, established feature branching strategy (`DIP-XX-...`), enforced PR peer review protocol, and initiated runnable API and ML starter code. | **Resolved** |

---

## 3. Key Decisions Directly Influenced by Supervisor Input

1. **Adoption of Spatial K-Fold Validation**: Under supervisor advice, we discarded standard random splitting to prevent optimistic bias caused by spatial autocorrelation (*Tobler's First Law*).
2. **Prioritization of Explainability**: Selected Tree SHAP explainability over opaque deep neural networks to ensure urban planners can interpret the physical rationale behind simulated thermal cooling.
3. **Structured Repository Layout**: Reorganized documentation into numbered, committee-aligned markdown artifacts (`docs/01_...` through `docs/11_...`) for rapid audit during pre-defense evaluation.
