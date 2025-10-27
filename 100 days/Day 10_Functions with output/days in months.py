
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False
        else: 
            return True
    else:
        return False
                
def days_in_month(year, month):
    """Checks if a year is a leap year or not and
        returns the (leap) year and number of days
        in the month inputed."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 31, 31, 31, 31]
    num_of_days = month_days[month - 1]
    if year < 1 and month > 12:
        return "kindly enter valid inputs: "
    else:
        if is_leap(year) == True:
            if month == 2:
                num_of_days += 1
            return f"The year {year} is a leap year with {num_of_days} days"
        elif is_leap(year) == False:
            return f"The year {year} is not a leap year with {num_of_days} days"

Leap_or_not = is_leap(year)
days = days_in_month(year, month)
print(days) 
