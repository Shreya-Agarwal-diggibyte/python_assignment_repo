import unittest

from src.no_idea.util import no_idea

class Test_no_idea(unittest.TestCase):
    def test_no_idea(self):
        n1, m1 = 3, 2
        array1 = [1, 5, 3]
        A1 = [3, 1]
        B1 = [5, 7]
        self.assertEqual(no_idea(n1, m1, array1, A1, B1), 1)
    def test_no_idea_2(self):
        n2, m2 = 4, 2
        array2 = [1, 2, 3, 4]
        A2 = [10, 20]
        B2 = [30, 40]
        self.assertEqual(no_idea(n2, m2, array2, A2, B2), 0)
    def test_no_idea_3(self):
        n3, m3 = 3, 1
        array3 = [2, 2, 2]
        A3 = [2]
        B3 = []
        self.assertEqual(no_idea(n3, m3, array3, A3, B3), 3)
    def test_no_idea_4(self):
        n4, m4 = 3, 2
        array4 = [9, 9, 9]
        A4 = []
        B4 = [9, 10]
        self.assertEqual(no_idea(n4, m4, array4, A4, B4), -3)
    def test_no_idea_5(self):
        n5, m5 = 6, 3
        array5 = [1, 2, 3, 4, 5, 1]
        A5 = [1, 3, 5]
        B5 = [2, 4, 6]
        self.assertEqual(no_idea(n5, m5, array5, A5, B5), 2)

if __name__ == '__main__':
    unittest.main()