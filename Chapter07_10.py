# 7.10 Write a test program that creates a Time object and displays its hour, minute, and second.
# Your program then prompts the user to enter an elapsed time, sets its elapsed time in the Time object,
# and displays its hour, minute, and second.
# Sample Input [55550505]

import time  # Import time module


class Time:

    # Construct a Time object that initializes hour, minute, and second using the current time
    def __init__(self, hour = 0, minute = 0, second = 0):
        # Get current time
        currentTime = time.time()

        # Compute the total seconds since midnight, Jan 1, 1970
        totalSeconds = int(currentTime)

        # Compute second and initialize second for the Time object
        self.__second = totalSeconds % 60

        # Compute the total minutes
        totalMinutes = totalSeconds // 60

        # Compute the minute in the hour and initialize minute for the Time object
        self.__minute = totalMinutes % 60

        # Compute the total hours
        totalHours = totalMinutes // 60

        # Compute the hour and initialize hour for the Time object
        self.__hour = totalHours % 24

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    # Set a new time for the object using the elapsed time in seconds
    def setTime(self, elapseTime):
        # Compute second and set it to second for the Time object
        self.__second = elapseTime % 60

        # Compute the total minutes
        totalMinutes = elapseTime // 60

        # Compute the minute and set it to minute for the Time object
        self.__minute = totalMinutes % 60

        # Compute the total hours
        totalHours = totalMinutes // 60

        # Compute the hour and and set it to hour for the Time object
        self.__hour = totalHours % 24


def main():
    # Create a Time object
    t1 = Time()

    # Display the hour, minute, second for this Time object
    print("Current time is " + str(t1.getHour()) + ":" + str(t1.getMinute()) + ":" \
          +str(t1.getSecond()))

    # Prompt the user to enter elapsed time
    elapseTime = eval(input("Enter the elapsed time: "))

    # Set new time for this Time object using the elapsed time in seconds
    t1.setTime(elapseTime)

    # Display the hour, minute, second for this Time object
    print("The hour:minute:second for the elapsed time is " + str(t1.getHour()) + ":" \
          +str(t1.getMinute()) + ":" + str(t1.getSecond()))


main()  # Call the main function
