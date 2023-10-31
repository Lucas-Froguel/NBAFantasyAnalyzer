from datetime import date
from datetime import timedelta


def get_first_and_last_day_of_week(today: date):
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=6)

    return start, end
