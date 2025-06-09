import unittest
from src.find_percentage.util import avg_calculation

class TestFindPercentage(unittest.TestCase):
    def test_find_percentage(self):
        student_data = [
            ("Alice", [80.0, 90.0, 100.0]),
            ("Bob", [70.0, 75.0, 80.0]),
            ("Charlie", [95.0, 85.0, 90.0])
        ]
        assert abs(avg_calculation(student_data, "Alice") - 90.0) < 1e-6
        assert abs(avg_calculation(student_data, "Bob") - 75.0) < 1e-6
        assert abs(avg_calculation(student_data, "Charlie") - 90.0) < 1e-6


if __name__ == "__main__":
    unittest.main()