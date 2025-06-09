import unittest
from src.word_order.util import count_words

class TestWordCounter(unittest.TestCase):
    def test_count_words(self):
        cases = [
            (["apple", "banana", "apple", "orange", "banana", "apple"], (["apple", "banana", "orange"], [3, 2, 1])),
            (["hello", "world", "hello"], (["hello", "world"], [2, 1])),
            (["test", "test", "test"], (["test"], [3])),
            ([], ([], [])),  # Edge case: no words
        ]

        for words, expected in cases:
            actual = count_words(words)
            self.assertEqual(actual, expected, f"Failed for input: {words}")

if __name__ == "__main__":
    unittest.main()
