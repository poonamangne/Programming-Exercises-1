# 4.21 Write a program that prompts the user to enter a year, month, and day of the month, 
# and then it displays the name of the day of the week

#Prompt the user for inputs
year = eval(input("Enter year: (e.g., 2008): "))
m = eval(input("Enter month: 1-12: "))
q = eval(input("Enter the day of the month: 1-31: "))

# Check if month is January or February and make adjustments to month and year
if (m == 1) or (m == 2):
    m = m + 12
    year = year - 1

# Compute the century and year of century
j = year // 100
k = year % 100

# Compute day of the week using Zeller's congruence
h = (q + 26 * (m + 1) // 10 + k + (k // 4) + (j // 4) + (5 * j)) % 7

# Compute day of the week
if h == 0:
    print("Day of the week is Saturday")
elif h == 1:
    print("Day of the week is Sunday")
elif h == 2:
    print("Day of the week is Monday")
elif h == 3:
    print("Day of the week is Tuesday")
elif h == 4:
    print("Day of the week is Wednesday")
elif h == 5:
    print("Day of the week is Thursday")
else:
    print("Day of the week is Friday")