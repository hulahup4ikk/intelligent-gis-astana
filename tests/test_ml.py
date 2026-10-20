import numpy as np
import pytest
from src.ml.indices import calculate_ndvi, calculate_ndwi, calculate_ndbi, estimate_lst_from_brightness_temp


def test_calculate_ndvi_green_vegetation():
    # NIR high, Red low -> high NDVI
    nir = np.array([[0.8, 0.7], [0.6, 0.9]])
    red = np.array([[0.1, 0.15], [0.1, 0.05]])
    ndvi = calculate_ndvi(nir, red)
    
    assert ndvi.shape == (2, 2)
    assert np.all(ndvi > 0.5)
    assert np.all(ndvi <= 1.0)


def test_calculate_ndvi_zero_division():
    nir = np.zeros((2, 2))
    red = np.zeros((2, 2))
    ndvi = calculate_ndvi(nir, red)
    assert np.all(ndvi == 0.0)


def test_calculate_ndbi_urban_impervious():
    # SWIR higher than NIR -> positive NDBI
    swir = np.array([[0.6, 0.5], [0.7, 0.65]])
    nir = np.array([[0.2, 0.25], [0.3, 0.2]])
    ndbi = calculate_ndbi(swir, nir)
    assert np.all(ndbi > 0.0)


def test_estimate_lst_celsius():
    # ~300 K brightness temperature should translate to ~27-32 C
    tb_kelvin = np.array([[305.0, 310.0], [295.0, 300.0]])
    lst_c = estimate_lst_from_brightness_temp(tb_kelvin, emissivity=0.98)
    
    # 305 K is approx 31.85 C
    assert np.all(lst_c > 20.0)
    assert np.all(lst_c < 45.0)
