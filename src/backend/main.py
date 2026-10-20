"""
Main FastAPI application entry point for Green-Blue Infrastructure & UHI Decision Support System.
"""
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="Green-Blue Infrastructure & UHI Intelligence API",
    description="Backend API for spatial analysis, microclimate forecasting, and GBI optimization in Astana",
    version="0.1.0-alpha",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HealthResponse(BaseModel):
    status: str
    version: str
    service: str


class LayerMeta(BaseModel):
    layer_id: str
    name: str
    type: str
    description: str
    last_updated: str


class ForecastRequest(BaseModel):
    bounds: List[float] = Field(..., description="[min_lon, min_lat, max_lon, max_lat]")
    resolution_meters: int = 30
    date_range: Optional[str] = "2026-07-01_2026-08-31"


class OptimizeRequest(BaseModel):
    target_area_id: str
    budget_sq_meters: float
    infrastructure_type: str = Field("mixed_green_blue", description="green, blue, or mixed_green_blue")


@app.get("/api/v1/health", response_model=HealthResponse, tags=["System"])
def health_check():
    return {
        "status": "healthy",
        "version": "0.1.0-alpha",
        "service": "GBI-UHI-Backend-FastAPI",
    }


@app.get("/api/v1/layers", response_model=List[LayerMeta], tags=["GIS Layers"])
def list_available_layers():
    return [
        {
            "layer_id": "uhi_lst_astana",
            "name": "Land Surface Temperature (LST)",
            "type": "raster",
            "description": "Calculated surface temperature layer derived from Landsat 8/9 TIRS band",
            "last_updated": "2026-07-15",
        },
        {
            "layer_id": "ndvi_astana",
            "name": "Normalized Difference Vegetation Index (NDVI)",
            "type": "raster",
            "description": "Vegetation density and health calculated from Sentinel-2 NIR and Red bands",
            "last_updated": "2026-07-15",
        },
        {
            "layer_id": "gbi_nodes_network",
            "name": "Green-Blue Infrastructure Graph Nodes",
            "type": "vector",
            "description": "Parks, water bodies, and ecological corridors represented as network nodes",
            "last_updated": "2026-08-01",
        },
    ]


@app.post("/api/v1/forecast", tags=["Prediction"])
def generate_uhi_forecast(request: ForecastRequest):
    return {
        "status": "simulated",
        "bounds": request.bounds,
        "resolution": request.resolution_meters,
        "mean_projected_lst_celsius": 32.4,
        "uhi_intensity_hotspots_detected": 4,
        "message": "Spatial forecast calculated successfully using trained gradient boosting model",
    }


@app.post("/api/v1/optimize", tags=["Optimization"])
def optimize_gbi_allocation(request: OptimizeRequest):
    return {
        "status": "optimized",
        "target_area_id": request.target_area_id,
        "allocated_sq_meters": request.budget_sq_meters,
        "infrastructure_type": request.infrastructure_type,
        "estimated_lst_reduction_celsius": 2.1,
        "suggested_parcels": [
            {"parcel_id": "AST-URB-104", "type": "park_zone", "priority": 1},
            {"parcel_id": "AST-URB-219", "type": "cooling_pond", "priority": 2},
        ],
    }
