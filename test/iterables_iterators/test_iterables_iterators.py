import unittest
from itertools import combinations
from src.iterables_iterators.util import iterables

class TestIterables(unittest.TestCase):
    def test_iterables(self):
        test_cases = [
            {
                "input": (4, ['a', 'b', 'c', 'd'], 2),
                "expected": 0.5  # Combinations: ab, ac, ad, bc, bd, cd -> 3 contain 'a'
            },
        {
            "input": (3, ['a', 'a', 'b'], 2),
            "expected": 1.0  # Combinations: aa, ab, ab -> all contain 'a'
        },
        {
            "input": (5, ['b', 'c', 'd', 'e', 'f'], 3),
            "expected": 0.0  # No combinations contain 'a'
        },
        {
            "input": (3, ['a', 'b', 'c'], 1),
            "expected": 1 / 3  # Combinations: a, b, c -> only 'a' contains 'a'
        },
        {
            "input": (0, [], 1),
            "expected": 0.0  # No elements to combine
        }
        ]

if __name__ == '__main__':
    unittest.main()



