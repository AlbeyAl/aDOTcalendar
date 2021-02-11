from django.http import HttpResponse
from calendar_index.date import Date

def calendar(request, year, month, day):
    class calendar_item(Date):
        def __init__(self, valid_date, date):
            self.valid_date = valid_date
            self.date = date

        def set_date(self, date):
            self.date = date

        def get_date(self):
            return self.date

    initial_date = Date(month, day, year)
    month_start = initial_date.get_start_day_of_week()
    month_length = initial_date.get_days_in_month()
    
    prev_month = initial_date.prev_month()
    next_month = initial_date.next_month()

    len_prev_month = month_start - 1
    len_next_month = 42 - (month_length - len_prev_month)

    start_prev_month = prev_month.get_days_in_month() - len_prev_month

    calendar_list = list()
    cal_day_count = 1
    valid_day_count = 1
    next_day_count = 1

    for week in range(6):
        calendar_list.append(list())
        for day in range(7):
            if cal_day_count < month_start:
                calendar_list[week].append(calendar_item(False, Date(prev_month.get_month(), start_prev_month + cal_day_count, prev_month.get_year())))
            
            if cal_day_count >= month_start and cal_day_count < (month_start + month_length):
                calendar_list[week].append(calendar_item(True, Date(initial_date.get_month(), valid_day_count, initial_date.get_year())))
                valid_day_count += 1

            if cal_day_count >= (month_start + month_length):
                calendar_list[week].append(calendar_item(False, Date(next_month.get_month(), next_day_count, next_month.get_year())))
                next_day_count += 1

            print(calendar_list[week][day].get_date())

            cal_day_count += 1

    return HttpResponse("TEST" + initial_date)