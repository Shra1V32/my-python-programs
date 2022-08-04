date = input("Enter the date in DD-MM-YYYY Format: ")
day, month, year = date.split('-')

day = int(day)
year = int(year)
month = int(month)

# Lets input 28-02-2022

# check if the month is leap year

if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month != 2:
    days = 30
elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    days = 29
else:
    days = 28

if month < 1 or month > 12 or day < 1 or day > days:
    print("Invalid date")
elif day == days and month != 12:
    day = 1
    month += 1
    print(f"Incremented date: {day}-{month}-{year}")
elif day == 31 and month == 12:
    day = 1
    month = 1
    year += 1
    print(f"Incremented date: {day}-{month}-{year}")
else:
    day = day+1
    print(f"Incremented date: {day}-{month}-{year}")
