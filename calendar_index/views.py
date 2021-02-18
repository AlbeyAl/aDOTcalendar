from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from calendar_index.date import Date
from calendar_index.models import Calendar, Event, ToDo, Check_List_Item
import datetime

def calendar(request, calendar_name, year, month, day):
    class Calendar_Item(Date):
        def __init__(self, valid_date, date, events, todos):
            # valid_date is used to determine if the current "date" is within the current month selected.
            # This allows me to decipher which square on the calendar UI to display or gray out.
            self.valid_date = valid_date
            self._current_day = False
            self.date = date
            self.events = list()
            self.todos = list()

            if (datetime.date.today().year == self.date.get_year()) and (datetime.date.today().month == self.date.get_month()) and (datetime.date.today().day == self.date.get_day()):
                self.current_day = True

            if events != None:
                self.events = events
            if todos != None:
                self.todos = todos

        def set_date(self, date):
            self.date = date

        def get_date(self):
            return self.date

        def current_day(self):
            return self._current_day

        def get_events_count(self):
            return len(self.events)

        def get_todos_count(self):
            return len(self.todos)

    context_data = None
        
    # Before proceeding with building the calendar, make sure the user is authenticated.
    # Otherwise redirect the current user to the login page.
    if request.user.is_authenticated:
        # Does a calendar + user exists?
        calendar_filter = Calendar.objects.filter(user=request.user, name=calendar_name)

        if calendar_filter.count() == 0:
            # Redirect to create new calendar.
            return HttpResponse("No calendars in database.")
        
        calendar_object = calendar_filter[0]

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
                    calendar_list[week].append(Calendar_Item(False, Date(prev_month.get_month(), start_prev_month + cal_day_count, prev_month.get_year()), None, None))
                
                if cal_day_count >= month_start and cal_day_count < (month_start + month_length):
                    temp_month = initial_date.get_month()
                    temp_day = valid_day_count
                    temp_year = initial_date.get_year()
                    date_converted = datetime.date(year=temp_year, month=temp_month, day=temp_day)

                    temp_calendar_item = Calendar_Item(True, Date(temp_month, temp_day, temp_year),
                        list(Event.objects.filter(date_created=date_converted, calendar=calendar_object)),
                        list(ToDo.objects.filter(date_created=date_converted, calendar=calendar_object)))

                    calendar_list[week].append(temp_calendar_item)
                    valid_day_count += 1

                if cal_day_count >= (month_start + month_length):
                    calendar_list[week].append(Calendar_Item(False, Date(next_month.get_month(), next_day_count, next_month.get_year()), None, None))
                    next_day_count += 1

                cal_day_count += 1

        context_data = {'calendar_list': calendar_list}    
    else:
        # Login redirect
        print("Not authenticated...")

    print(datetime.date.today().day)
    context_data['current_month'] = datetime.date.today().month
    context_data['current_day'] = datetime.date.today().day
    context_data['current_year'] = datetime.date.today().year

    return render(request, 'index/index.html', context=context_data)
