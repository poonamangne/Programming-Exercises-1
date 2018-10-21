# 2.7 Write a program that prompts the user to enter the minutes (e.g., 1 billion), 
# and displays the number of years and days for the minutes
# Sample Input[1000000000]

# Prompt the user to enter minutes
totalMinutes = eval(input("Enter the number of minutes: "))

# Compute minutes per day
minutesPerDay = 24 * 60

# Compute minutes per year
minutesPerYear = 365 * minutesPerDay

# Compute number of years
numberOfYears = totalMinutes // minutesPerYear

# Compute number of days remaining
remainingDays = (totalMinutes % minutesPerYear) // minutesPerDay

# Display result
print(totalMinutes, "minutes is approximately", numberOfYears, "years and", remainingDays, "days")