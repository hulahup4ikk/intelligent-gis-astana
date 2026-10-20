# Development of an Intelligent Geographic Information System for Graph-Based Analysis, Forecasting, and Optimization of Green-Blue Infrastructure to Mitigate the Urban Heat Island Effect in Astana

[![Status: Pre-Defense 1](https://img.shields.io/badge/Status-Pre--Defense%201%20(Draft)-orange)]()
[![Python: 3.11+](https://img.shields.io/badge/Python-3.11+-blue)]()
[![License: Academic](https://img.shields.io/badge/License-Academic%20Diploma-green)]()

## 1. Project Title and Brief Description
**Интеллектуальная геоинформационная система (ГИС) на основе графового анализа, прогнозирования и многокритериальной оптимизации зелено-голубой инфраструктуры для снижения эффекта городского острова тепла в городе Астане.**

Проект представляет собой программно-аналитический комплекс, объединяющий методы дистанционного зондирования Земли (ДЗЗ), пространственного анализа, машинного обучения и графовой оптимизации для выявления зон термического дискомфорта (Urban Heat Island — UHI) и генерации научно обоснованных сценариев размещения зеленых насаждений и водных коридоров (Green-Blue Infrastructure — GBI) на территории города Астаны.

---

## 2. Problem Statement, Target Users, and Expected Outcomes

### Проблематика (Problem Statement)
Город Астана подвержен выраженному эффекту городского острова тепла (UHI) в летний период из-за высокой доли искусственных водонепроницаемых поверхностей (асфальт, бетон), плотной многоэтажной застройки и фрагментированности существующего озеленения. Существующие градостроительные решения принимаются без регулярного анализа мультиспектральных спутниковых данных и математического моделирования охлаждающего эффекта зелено-голубой инфраструктуры.

### Целевые пользователи (Target Users)
1. **Управление архитектуры, градостроительства и земельных отношений г. Астаны** — планирование генерального плана, парковых зон и рекреационных каркасов.
2. **Департамент экологии и природопользования** — мониторинг микроклиматических рисков, зон термического перегрева и состояния растительного покрова.
3. **Городские урбанисты, исследователи и ситуационные центры** — моделирование климатических сценариев и оценка эффективности зеленых коридоров.

### Ожидаемые результаты (Expected Outcomes)
- Автоматизированный пайплайн сбора и предобработки спутниковых снимков (Sentinel-2, Landsat 8/9) с расчетом климатических индексов LST, NDVI, NDWI, NDBI.
- Модель машинного обучения прогнозирования температуры поверхности суши (LST) с точностью $R^2 \ge 0.75$.
- Графовая модель связанности эколого-рекреационного каркаса города.
- Алгоритм многокритериальной оптимизации (GA / NSGA-II) для выбора оптимальных локаций новых зеленых зон и водных объектов.
- Интерактивный веб-дашборд (React, Mapbox GL / Leaflet, FastAPI) для визуализации тепловых карт и сценариев оптимизации.

---

## 3. Team Members, Responsibilities, and Supervisor

| Роль | ФИО | Контакты | Основные зоны ответственности |
|---|---|---|---|
| **Machine Learning & Spatial Data Science Engineer** | **Кузнецов Иван Алексеевич** | `241258@astanait.edu.kz` | Пайплайн ДЗЗ (Sentinel/Landsat), расчет индексов LST/NDVI/NDWI, разработка и валидация ML-моделей прогнозирования UHI, алгоритмы оптимизации GBI, ведение репозитория и YouTrack |
| **Backend, GIS & Text Analytics Engineer** | **Байгулов Жетпіс Шайзадаұлы** | `242181@astanait.edu.kz` | Проектирование геобазы PostGIS, модуль графового анализа связанности, серверный REST API (FastAPI), веб-дашборд, пользовательские исследования и UX-сценарии |
| **Научный руководитель (Supervisor)** | **Макатов Арстан Кутжанович** | Сеньор-лектор Школы программной инженерии Astana IT University | Общее научное руководство, валидация методологии и архитектурных решений, регулярный контроль этапов |

---

## 4. Project Scope and Current Development Status

- **Текущий этап**: **Pre-defense 1 (24 октября 2026 г.)**.
- **Статус выполнения**:
  - [x] Определение целей, скоупа и паспорта проекта (Project Proposal).
  - [x] Анализ актуальности и проектирование исследования пользователей.
  - [x] Литературный обзор предметной области ($\ge 12$ источников, $\ge 8$ научных публикаций).
  - [x] Сравнение существующих ГИС и климатических решений (InVEST, ENVI-met, QGIS).
  - [x] Анализ технологического стека (ДЗЗ, ML, бэкенд, PostGIS).
  - [x] Разработка функциональных (FR) и нефункциональных (NFR) требований MoSCoW.
  - [x] Проектирование архитектуры (System Context, Use Case, ML Data Flow).
  - [x] Разработка UX-мокапов интерфейса и каркаса API.
  - [x] План верификации и оценки точности моделей.
  - [x] Настройка проектного управления в YouTrack и структуры Git.

---

## 5. Selected Technologies

- **Сбор и анализ данных ДЗЗ**: Python, Google Earth Engine API, Sentinel Hub API, GeoPandas, Rasterio, Shapely, NumPy.
- **Машинное обучение и оптимизация**: Scikit-Learn, XGBoost, LightGBM, PyGAD / DEAP (генетические алгоритмы).
- **Графовый анализ**: NetworkX, OSMnx.
- **Бэкенд и СУБД**: FastAPI, PostgreSQL 16 + PostGIS, SQLAlchemy, Pydantic.
- **Фронтенд и ГИС-визуализация**: React, TypeScript, Mapbox GL JS / Leaflet, Tailwind CSS.
- **Инфраструктура и управление**: Docker, GitHub, YouTrack.

---

## 6. Project Documentation & Management Links

Все обязательные компоненты предзащиты оформлены в директории `docs/`:

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

- **YouTrack Project**: [DIP: GBI-UHI Astana](https://gbi-uhi-astana.youtrack.cloud/projects/DIP) *(Задачи DIP-1 ... DIP-14)*
- **Wireframes & Prototype**: см. [docs/08_prototype/](docs/08_prototype/) *(UX-сценарии и мокапы интерфейса)*

---

## 7. Setup, Execution, and Testing Instructions

### Предварительные требования
- Python 3.11+
- Git

### Установка зависимостей
```bash
# Клонирование репозитория
git clone https://github.com/hulahup4ikk/intelligent-gis-astana.git
cd intelligent-gis-astana

# Создание и активация виртуального окружения
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
```

### Запуск прототипа API
```bash
uvicorn src.backend.main:app --reload --port 8000
```
Документация Swagger UI доступна по адресу: `http://localhost:8000/docs`

### Запуск тестов
```bash
pytest tests/
```
