import unittest
from src.minimum_maximum.util import min_max

class Test(unittest.TestCase):
    def test_min_max(self):
        arr1 = [
            [3, 1, 2],
            [4, 4, 5],
            [1, 2, 3]
        ]
        expected1 = 4
        actual1 = min_max(arr1)
        self.assertEqual(min_max(arr1),expected1)

    def test_min_max2(self):
        arr = [
            [7, 8, 9],
            [2, 3, 4]
        ]
        expected2 = 7
        actual2 = min_max(arr)
        self.assertEqual(actual2,expected2)


if __name__ == '__main__':
    unittest.main()