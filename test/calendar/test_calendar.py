import unittest

from src.calendar.util import calendar_module


class TestCalendar(unittest.TestCase):
    def test_weekday_name_1(self):
        date_str="01-09-2000"
        actual_weekday_name = calendar_module(date_str)
        expected_weekday_name = "SUNDAY"
        self.assertEqual(actual_weekday_name, expected_weekday_name)

    def test_weekday_name_2(self):
        date_str="01-09-2013"
        actual_weekday_name = calendar_module(date_str)
        expected_weekday_name = "WEDNESDAY"
        self.assertEqual(actual_weekday_name, expected_weekday_name)


if __name__ == '__main__':
    unittest.main()