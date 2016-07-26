from datetime import datetime

import pandas as pd

from src.beans.QueryInfo import QueryInfo


def generate_query(year_start, month_start, day_start, state, city):
    date_list = pd.date_range(start=datetime(year=year_start, month=month_start, day=day_start),
                              end=(pd.datetime.today()-pd.DateOffset(days=1))).tolist()

    query_list = []
    for date in date_list:
        query_list.append(QueryInfo(date.year, date.month, date.day, state, city))

    return query_list
