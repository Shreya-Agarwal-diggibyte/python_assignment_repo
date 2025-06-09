import unittest
from src.piling_up.util import piling_up

class Test_Piling_Up(unittest.TestCase):
    def test_piling_up(self):
        test_cases1 = [
            [1, 2, 3, 4, 5],  # Possible to pile up
            [5, 4, 3, 2, 1],  # Possible to pile up
            [1, 3, 2, 4],  # Not possible to pile up
        ]
        expected1 = ["Yes", "Yes", "No"]
        self.assertEqual(piling_up(test_cases1), expected1)
    def test_piling_up2(self):
        test_cases2 = [
            [1],
            [2],
        ]
        expected2 = ["Yes", "Yes"]
        self.assertEqual(piling_up(test_cases2), expected2)

if __name__ == '__main__':
    unittest.main()