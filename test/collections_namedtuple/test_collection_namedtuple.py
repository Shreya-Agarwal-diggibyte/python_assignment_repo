import unittest
from src.collections_namedtuple.util import named_tuple

class TestNamedTuple(unittest.TestCase):
    def test_named_tuple(self):
        total_students = 3
        columns = ['NAME', 'MARKS']
        student_data = [
            "Shreya 85",
            "Shiva 90",
            "Gori 75"
        ]
        self.assertEqual(named_tuple(total_students, columns, student_data), 83.33333333333333)



if __name__ == '__main__':
    unittest.main()
