# 4.5 Write a program that prompts the user to enter an integer for today’s day of the week
# (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also prompt the user to enter the number of days 
# after today for a future day and display the future day of the week

# Prompt the user to enter an integer for today’s day of the week
todayNumber = eval(input("Enter today's day: "))
             
# Prompt the user to enter the number of days after today for a future day
numberOfDays = eval(input("Enter the number of days elapsed since today: "))

# Compute future day number
futureDayNumber = (todayNumber + numberOfDays) % 7

# Get day of the week for today
if todayNumber == 0:
    today = "Sunday"
elif todayNumber == 1:
    today = "Monday"
elif todayNumber == 2:
    today = "Tuesday"
elif todayNumber == 3:
    today = "Wednesday"
elif todayNumber == 4:
    today = "Thursday"
elif todayNumber == 5:
    today = "Friday"
else:
    today = "Saturday"

# Get day of the week for future day
if futureDayNumber == 0:
    futureDay = "Sunday"
elif futureDayNumber == 1:
    futureDay = "Monday"
elif futureDayNumber == 2:
    futureDay = "Tuesday"
elif futureDayNumber == 3:
    futureDay = "Wednesday"
elif futureDayNumber == 4:
    futureDay = "Thursday"
elif futureDayNumber == 5:
    futureDay = "Friday"
else:
    futureDay = "Saturday"
    
# Display the future day of the week
print("Today is", today, "and the future day is", futureDay)
