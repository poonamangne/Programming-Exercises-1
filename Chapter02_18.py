# 2.18 Write a program that prompts the user to enter the time zone in hours away from (offset to) GMT 
# and displays the time in the specified time zone

import time # Import time module

# Prompt the user to enter the time zone in hours away from (offset to) GMT
offsetHours = eval(input("Enter the time zone in hours away from (offset to) GMT: "))

# Convert time zone hours to seconds
offsetSeconds = int(offsetHours * 60 * 60)

# Get current time
currentTime = time.time() 

# Compute the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# Compute the total seconds after time zone adjustment
totalSeconds = totalSeconds + offsetSeconds

# Compute current second
currentSecond = totalSeconds % 60

# Compute the total minutes
totalMinutes = totalSeconds // 60

# Compute the current minute in the hour
currentMinute = totalMinutes % 60

# Compute the total hours
totalHours = totalMinutes // 60

# Compute the current hour
currentHour = totalHours % 24

# Display the time in the specified time zone
print("The current time is", currentHour, ":", currentMinute,":", currentSecond)