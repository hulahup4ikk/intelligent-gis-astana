"""
Module for computing Remote Sensing & Climate Indices (NDVI, NDWI, NDBI, LST)
for Urban Heat Island and Green-Blue Infrastructure Analysis in Astana.
Author: Ivan Kuznetsov (Machine Learning & Spatial Data Science Engineer)
"""

import numpy as np
from typing import Tuple, Union


def calculate_ndvi(nir_band: np.ndarray, red_band: np.ndarray) -> np.ndarray:
    """
    Calculate Normalized Difference Vegetation Index (NDVI).
    NDVI = (NIR - RED) / (NIR + RED)
    Ranges from -1.0 to +1.0. High values (> 0.4) indicate healthy green vegetation.
    """
    nir = nir_band.astype(np.float64)
    red = red_band.astype(np.float64)
    denominator = nir + red
    
    # Avoid division by zero
    with np.errstate(divide='ignore', invalid='ignore'):
        ndvi = np.where(denominator != 0, (nir - red) / denominator, 0.0)
    
    return np.clip(ndvi, -1.0, 1.0)


def calculate_ndwi(nir_band: np.ndarray, swir_band: np.ndarray) -> np.ndarray:
    """
    Calculate Normalized Difference Water Index (NDWI) / McFeeters or Gao variant.
    NDWI = (NIR - SWIR) / (NIR + SWIR)
    Ranges from -1.0 to +1.0. Higher values indicate open water or high moisture.
    """
    nir = nir_band.astype(np.float64)
    swir = swir_band.astype(np.float64)
    denominator = nir + swir

    with np.errstate(divide='ignore', invalid='ignore'):
        ndwi = np.where(denominator != 0, (nir - swir) / denominator, 0.0)

    return np.clip(ndwi, -1.0, 1.0)


def calculate_ndbi(swir_band: np.ndarray, nir_band: np.ndarray) -> np.ndarray:
    """
    Calculate Normalized Difference Built-up Index (NDBI).
    NDBI = (SWIR - NIR) / (SWIR + NIR)
    Positive values correspond to urban impervious surfaces (concrete, asphalt).
    """
    swir = swir_band.astype(np.float64)
    nir = nir_band.astype(np.float64)
    denominator = swir + nir

    with np.errstate(divide='ignore', invalid='ignore'):
        ndbi = np.where(denominator != 0, (swir - nir) / denominator, 0.0)

    return np.clip(ndbi, -1.0, 1.0)


def estimate_lst_from_brightness_temp(
    brightness_temp_kelvin: np.ndarray,
    emissivity: Union[float, np.ndarray] = 0.98,
    wavelength_micrometers: float = 10.895
) -> np.ndarray:
    """
    Calculate Land Surface Temperature (LST) in Celsius using the Split-Window / Artis & Carnahan algorithm:
    LST = TB / (1 + (lambda * TB / rho) * ln(epsilon)) - 273.15
    where:
      TB = at-sensor brightness temperature (K)
      lambda = wavelength of emitted radiance (~10.895 um for Landsat 8 Band 10)
      rho = h * c / sigma = 1.438 * 10^-2 m K = 14380 um K
      epsilon = land surface emissivity
    """
    rho = 14380.0  # um * K
    tb = brightness_temp_kelvin.astype(np.float64)
    
    lst_kelvin = tb / (1.0 + (wavelength_micrometers * tb / rho) * np.log(emissivity))
    lst_celsius = lst_kelvin - 273.15
    return lst_celsius
