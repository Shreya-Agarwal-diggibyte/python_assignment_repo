import unittest
import numpy as np
from src.mean_var_std.util import find_mean_var_std

class Test(unittest.TestCase):
    def test_find_mean_var_std(self):
        test_cases = [
            {
                "input": np.array([[1, 2, 3], [4, 5, 6]]),
                "expected_mean": np.array([2.0, 5.0]),
                "expected_var": np.array([4.5, 4.5, 4.5]),
                "expected_std": 1.707825127659933
            },
            {
                "input": np.array([[0, 0, 0], [0, 0, 0]]),
                "expected_mean": np.array([0.0, 0.0]),
                "expected_var": np.array([0.0, 0.0, 0.0]),
                "expected_std": 0.0
            },]

if __name__ == '__main__':
    unittest.main()
