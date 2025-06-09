import calendar
import datetime

def calendar_module(date_val):
    input_val = input("Enter a date (MM-DD-YYYY)").split('-')
    month=int(input_val[0])
    day=int(input_val[1])
    year=int(input_val[2])
    weekday_index = calendar.weekday(year , month , day)

    weekday_name = calendar.day_name[weekday_index]

    return weekday_name.upper()

