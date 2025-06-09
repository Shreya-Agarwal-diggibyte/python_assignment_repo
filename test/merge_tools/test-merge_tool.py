import unittest

from numpy.ma.core import equal

from src.merge_the_tools.util import merge_the_tools

class TestMergeTools(unittest.TestCase):
    def test_merge_tool(self):
        # Test case 1
        actual = merge_the_tools("AABCAAADA", 3)
        expected = ["AB", "CA", "AD"]
        assert actual == expected, f"Test case 1 failed: expected {expected}, got {actual}"
    def test_merge_tool_2(self):
        # Test case 2
        actual = merge_the_tools("AAABBBCCC", 3)
        expected = ["AB", "BC", "C"]
        assert actual == expected, f"Test case 2 failed: expected {expected}, got {actual}"
    def test_merge_tool_3(self):
        # Test case 3
        actual = merge_the_tools("ABCDE", 2)
        expected = ["AB", "CD", "E"]
        assert actual == expected, f"Test case 3 failed: expected {expected}, got {actual}"
    def test_merge_tool_4(self):
        # Test case 4
        actual = merge_the_tools("NNNNNNNN", 4)
        expected = ["N", "N"]
        assert actual == expected, f"Test case 4 failed: expected {expected}, got {actual}"
    def test_merge_tool_5(self):
        # Test case 5
        actual = merge_the_tools("XYZXYZXYZ", 3)
        expected = ["XYZ", "XYZ", "XYZ"]
        self.assertEqual(actual,expected)
    def test_merge_tool_6(self):
        # Test case 6 - empty string
        actual = merge_the_tools("", 1)
        expected = []
        assert actual == expected, f"Test case 6 failed: expected {expected}, got {actual}"

if __name__ == '__main__':
    unittest.main()