
def isLeapYear(year):
    if year % 4 != 0:
        return "Not a leap year"
    elif year % 100 != 0:
        return "Leap year"
    elif year % 400 == 0:
        return "Leap year"
    else:
        return "Not a leap year"

year = 2000
print(f"{year} is {isLeapYear(year)}") # leap year
year = 2026
print(f"{year} is {isLeapYear(year)}") # not a leap year
