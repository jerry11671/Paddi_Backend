import calendar
from datetime import datetime


def get_days_in_month(month):
    current_year = datetime.now().year
    return calendar.monthrange(current_year, month)
