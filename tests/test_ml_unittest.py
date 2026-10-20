import unittest
import numpy as np
from src.ml.indices import calculate_ndvi, calculate_ndwi, calculate_ndbi, estimate_lst_from_brightness_temp


class TestMLIndices(unittest.TestCase):
    def test_calculate_ndvi(self):
        nir = np.array([[0.8, 0.7], [0.6, 0.9]])
        red = np.array([[0.1, 0.15], [0.1, 0.05]])
        ndvi = calculate_ndvi(nir, red)
        self.assertEqual(ndvi.shape, (2, 2))
        self.assertTrue(np.all(ndvi > 0.5))
        self.assertTrue(np.all(ndvi <= 1.0))

    def test_calculate_ndbi(self):
        swir = np.array([[0.6, 0.5], [0.7, 0.65]])
        nir = np.array([[0.2, 0.25], [0.3, 0.2]])
        ndbi = calculate_ndbi(swir, nir)
        self.assertTrue(np.all(ndbi > 0.0))

    def test_estimate_lst(self):
        tb_kelvin = np.array([[305.0, 310.0], [295.0, 300.0]])
        lst_c = estimate_lst_from_brightness_temp(tb_kelvin, emissivity=0.98)
        self.assertTrue(np.all(lst_c > 20.0))
        self.assertTrue(np.all(lst_c < 45.0))


if __name__ == '__main__':
    unittest.main()
