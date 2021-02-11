import math

class Date():
    def __init__(self, m, d, y):
        self.month = m
        self.day = d
        self.year = y

    def __str__(self):
        return "Date (M/D/YYYY): " + str(self.get_month()) + '/' + str(self.get_day()) + '/' + str(self.get_year())

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_year(self):
        return self.year

    def get_days_in_month(self):
        results = None

        if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
            results = 31
        elif self.month == 2:
            if self.is_leap_year():
                results = 29
            else:
                results = 28
        else:
            results = 30

        return results

    def get_start_day_of_week(self):
        results = 0

        month_code = {1: 11, 2: 12, 3: 1, 4: 2, 5: 3,
                      6: 4, 7: 5, 8: 6, 9: 7, 10: 8, 11: 9, 12: 10}

        k = 1
        m = month_code[self.month]
        C = 20
        D = self.year % 100

        if m == 11 or m == 12:
            D -= 1

        f = k + math.floor((13*m-1) / 5) + D + \
            math.floor(D/4) + math.floor(C/4) - 2 * C

        results = (f % 7)

        # The reason for adding one to the results is because the formula starts at zero and counts up.
        # For instance, if the start of the month falls on the first day of the week it would return a zero, but
        # if it falls on the second day of the week it would return a one. By adding the one to the results makes
        # future calculations easier for the end user.

        return results + 1

    def is_leap_year(self):
        results = False

        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    results = True
                else:
                    results = False
            else:
                results = True
        else:
            results = False

        return results

    def valid_month(self):
        results = True

        if self.month < 1 or self.month > 12:
            results = False

        return results

    def valid_day(self):
        results = True

        if self.valid_month:
            if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:
                if self.day < 1 or self.day > 31:
                    results = False
                else:
                    results = True
            elif self.month == 2:
                if self.is_leap_year():
                    if self.day < 1 or self.day > 29:
                        results = False
                    else:
                        results = True
                else:
                    if self.day < 1 or self.day > 28:
                        results = False
                    else:
                        results = True
            elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
                if self.day < 1 or self.day > 30:
                    results = False
                else:
                    results = True
            else:
                # not a valid given day:
                results = False
        else:
            results = False

        return results

    def valid_year(self):
        return not self.year < 0

    def valid_date(self):
        return self.valid_month() and self.valid_day() and self.valid_year()

    def prev_month(self):
        new_year = self.get_year()
        new_month = self.get_month() - 1

        if self.get_month() == 1:
            new_year -= 1
            new_month = 12

        return Date(new_month, 1, new_year)

    def next_month(self):
        new_year = self.get_year()
        new_month = self.get_month() + 1

        if self.get_month() == 12:
            new_year += 1
            new_month = 1

        return Date(new_month, 1, new_year)
