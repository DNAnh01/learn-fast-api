from datetime import datetime, timedelta
from typing import List


def generate_dates_in_range(start: datetime, end: datetime) -> List[str]:
    """
    Generate a list of dates in the range of start and end date
    :param start: start date
    :param end: end date
    :return: List string of dates in the range

    e.g.
    start = datetime(2024, 1, 1)
    end = datetime(2024, 1, 5)
    generate_dates_in_range(start, end) -> ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05']
    """
    date_format = "%Y-%m-%d"
    date_list = []
    current_date = start
    while current_date <= end:
        date_list.append(current_date.strftime(date_format))
        current_date += timedelta(days=1)
    return date_list
