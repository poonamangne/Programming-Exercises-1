# 5.30 Write a program that prompts the user to enter the year and first day of the year,
# and displays the first day of each month in the year on the console

# Prompt the user for inputs
year, firstDayOfYear = eval(input("Enter the year and first day of the year(e.g 2016, 3): "))

# Check if the given year is a leap year
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    isLeapYear = True
else:
    isLeapYear = False

# Compute the first day number for each month and display result
for i in range(1, 13):
    if i == 1:
        dayNumber = firstDayOfYear
        month = "January"
        numberOfDaysInMonth = 31
    else:
        dayNumber = (firstDayOfYear + numberOfDaysInMonth) % 7
        if i == 2:
            month = "February"
            # Check for leap year and set number of days accordingly
            if isLeapYear:
                numberOfDaysInMonth += 29
            else:
                numberOfDaysInMonth += 28
        elif i == 3:
            month = "March"
            numberOfDaysInMonth += 31
        elif i == 4:
            month = "April"
            numberOfDaysInMonth += 30
        elif i == 5:
            month = "May"
            numberOfDaysInMonth += 31
        elif i == 6:
            month = "June"
            numberOfDaysInMonth += 30
        elif i == 7:
            month = "July"
            numberOfDaysInMonth += 31
        elif i == 8:
            month = "August"
            numberOfDaysInMonth += 31
        elif i == 9:
            month = "September"
            numberOfDaysInMonth += 30
        elif i == 10:
            month = "October"
            numberOfDaysInMonth += 31
        elif i == 11:
            month = "November"
            numberOfDaysInMonth += 30
        else:
            month = "December"
            numberOfDaysInMonth += 31

    # Compute day from day number
    if dayNumber == 0:
        day = "Sunday"
    elif dayNumber == 1:
        day = "Monday"
    elif dayNumber == 2:
        day = "Tuesday"
    elif dayNumber == 3:
        day = "Wednesday"
    elif dayNumber == 4:
        day = "Thursday"
    elif dayNumber == 5:
        day = "Friday"
    else:
        day = "Saturday"

    # Display result
    print(month, "1", year, "is", day)
