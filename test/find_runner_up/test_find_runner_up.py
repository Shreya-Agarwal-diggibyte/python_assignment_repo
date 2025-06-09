import unittest
from src.find_runner_up.util import unique_value

class TestFindRunnerUp(unittest.TestCase):
    def test_find_runner_up(self):
        test_cases = [
            {
                "input": [1, 2, 2, 3, 4, 4, 5],
                "expected": [1, 2, 3, 4, 5]
            },
            {
                "input": [5, 5, 5, 5],
                "expected": [5]
            },
            {
                "input": [3, 1, 2, 2, 3, 4],
                "expected": [1, 2, 3, 4]
            },
            {
                "input": [],
                "expected": []
            },
            {
                "input": [10, 20, 10, 30, 20, 40],
                "expected": [10, 20, 30, 40]
            }
            ]

if __name__ == "__main__":
    unittest.main()
