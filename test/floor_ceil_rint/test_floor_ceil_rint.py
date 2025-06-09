import unittest
import numpy as np
from src.floor_ceil_rint.util import find_floor_ceil_rint

class TestFloorCeilRint(unittest.TestCase):
    def test_floor_ceil_rint(self):
        test_cases = [
            {
                "input": np.array([1.5, 2.3, 3.7]),
                "expected": (np.array([1.0, 2.0, 3.0]), np.array([2.0, 3.0, 4.0]), np.array([2.0, 2.0, 4.0]))
            },
            {
                "input": np.array([-1.5, -2.3, -3.7]),
                "expected": (np.array([-2.0, -3.0, -4.0]), np.array([-1.0, -2.0, -3.0]), np.array([-2.0, -2.0, -4.0]))
            },
            {
                "input": np.array([0.0, 0.5, -0.5]),
                "expected": (np.array([0.0, 0.0, -1.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 0.0, -1.0]))
            },
            {
                "input": np.array([2.0, 3.0, 4.0]),
                "expected": (np.array([2.0, 3.0, 4.0]), np.array([2.0, 3.0, 4.0]), np.array([2.0, 3.0, 4.0]))
            }
        ]


if __name__ == "__main__":
    unittest.main()