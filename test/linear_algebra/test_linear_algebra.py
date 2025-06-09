import unittest
import numpy as np
from src.linear_algebra.util import find_linear_algebra

class TestLinearAlgebra(unittest.TestCase):
    def test_find_linear_algebra(self):
        test_cases = [
            {
                "input": [[1, 2], [3, 4]],
                "expected": -2.0
            },
        {
            "input": [[2, 0], [0, 2]],
            "expected": 4.0
        },
        {
            "input": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "expected": 0.0
        },
        {
            "input": [[3]],
            "expected": 3.0
        },
        {
            "input": [[0, 0], [0, 0]],
            "expected": 0.0
        }

    ]

if __name__ == '__main__':
    unittest.main()