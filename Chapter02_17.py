# 2.17 Write a program that prompts the user to enter a weight in pounds and height in inches 
# and displays the BMI
# Sample Inputs [95.5. 50]

# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds: "))

# Prompt the user to enter height in inches
height = eval(input("Enter height in inches: "))

# Constants
KILOGRAM_PER_POUND = 0.45359237
METER_PER_INCH = 0.0254

# Convert weight in pounds to kilograms
weightInKilograms = weight * KILOGRAM_PER_POUND

# Convert height in inches to meters
heightInMeters = height * METER_PER_INCH

# Compute BMI
bmi = weightInKilograms / (heightInMeters ** 2)

# Display result with four digits after decimal point
print("BMI is", round(bmi * 10000) / 10000.0)