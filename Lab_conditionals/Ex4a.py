year = 2026

is_leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(year, "is a leap year:", is_leap_year)

