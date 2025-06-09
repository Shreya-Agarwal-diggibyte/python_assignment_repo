import unittest
from src.string_mutations.util import mutate_string

class TestMutateString(unittest.TestCase):
    def test_mutate_string(self):
        self.assertEqual(mutate_string("hello", 0, "y"), "yello")
        self.assertEqual(mutate_string("world", 4, "d"), "world")
        self.assertEqual(mutate_string("python", 3, "s"), "pytson")
        self.assertEqual(mutate_string("mutation", 7, "s"), "mutatios")
        self.assertEqual(mutate_string("abcde", 2, "Z"), "abZde")

if __name__ == "__main__":
    unittest.main()