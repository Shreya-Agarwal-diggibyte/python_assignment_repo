import unittest
from src.string_formatting.util import print_formatted

class TestStringFormatting(unittest.TestCase):
    def test_print_formatted(self):
        expected_output_1 = '   1   1   1   1'
        self.assertEqual(print_formatted(1), expected_output_1)
    def test_print_formatted2(self):
        expected_output_2 = (
            "1  1  1  1\n"
            "2  2  2 10"
        )
        self.assertEqual(print_formatted(2), expected_output_2)


if __name__ == '__main__':
    unittest.main()