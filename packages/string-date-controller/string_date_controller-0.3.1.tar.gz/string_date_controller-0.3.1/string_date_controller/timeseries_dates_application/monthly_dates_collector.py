from string_date_controller.date_determinator import is_month_end
from string_date_controller.date_shifter import (
    get_last_date_of_month, 
    get_date_n_months_ago
)

def get_month_end_dates(dates):
    dates_month_end = list(filter(is_month_end, dates))
    if not dates_month_end:
        dates_month_end = [dates[-1]]
    return dates_month_end

def adjust_first_and_last_date(dates, min_date, max_date):
    first_date = max(dates[0], min_date)
    last_date = min(dates[-1], max_date)
    return [first_date] + dates[1:-1] + [last_date]

def get_prev_month_end_dates_with_adjustment(dates):
    month_end_dates = get_month_end_dates(dates)
    dates = adjust_first_and_last_date(
        list(map(
            lambda date: get_last_date_of_month(get_date_n_months_ago(date, 1)), 
            month_end_dates
        )),
        dates[0],
        dates[-1]
    )
    return dates

def has_dummy_pair_in_date_pairs(date_pairs):
    return date_pairs[0][0] == date_pairs[0][1]


def get_monthly_date_pairs(dates):
    first_date = dates[0]
    last_date = dates[-1]
    month_end_dates = get_month_end_dates(dates)
    prev_month_end_dates = adjust_first_and_last_date(
        list(map(
            lambda date: get_last_date_of_month(get_date_n_months_ago(date, 1)), 
            month_end_dates
        )),
        first_date,
        last_date
    )
    date_pairs = list(zip(prev_month_end_dates, month_end_dates))
    if last_date not in month_end_dates:
        date_pairs.append((month_end_dates[-1], last_date))
    if has_dummy_pair_in_date_pairs(date_pairs):
        date_pairs = date_pairs[1:]
    return date_pairs

def map_date_pairs_to_dict(date_pairs):
    dct = {}
    for date_pair in date_pairs:
        year, month, _ = date_pair[-1].split('-')
        dct[f'{year}-{month}'] = date_pair
    return dct

def get_all_data_monthly_date_pairs(dates):
    date_pairs = get_monthly_date_pairs(dates)
    return map_date_pairs_to_dict(date_pairs)