#Function with input and output
def is_leap(year):
    """return is that its leap year"""
    if year %4 == 0:
        if year %100 ==0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def day_in_months(year,month):
    monts_in_year =[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month ==2:
        return 29
    return monts_in_year[month-1]
years = int(input("Enter the year: "))
months =int(input("Enter the months: "))

days = day_in_months(years,months)
print(days)