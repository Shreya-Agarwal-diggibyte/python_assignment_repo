import unittest
from src.time_delta.util import time_delta

class TestTimeDelta(unittest.TestCase):
    def test_time_delta(self):
        cases = [
            # (t1, t2, expected_output)
            ("Sun 10 May 2015 13:54:36 +0000", "Sun 10 May 2015 13:54:36 +0000", "0"),
            ("Sun 10 May 2015 13:54:36 +0000", "Sun 10 May 2015 14:54:36 +0000", "3600"),
            ("Sun 10 May 2015 10:54:36 +0000", "Sun 10 May 2015 14:54:36 +0000", "14400"),
            ("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000", "88200"),
        ]
        for t1, t2, expected in cases:
            actual = time_delta(t1, t2)
            self.assertEqual(actual, expected, f"Failed for inputs: {t1} and {t2}")

if __name__ == "__main__":
    unittest.main()
