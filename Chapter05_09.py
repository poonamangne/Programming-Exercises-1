# 5.9 Write a program that computes the tuition in ten years and the total cost of 
# four years’ worth of tuition starting ten years from now.

PERCENTAGE_INCREASE = 0.05 # Constant
tuition = 10000 # Tuition this year
count = 0 # Initialize count for number of years
fourYearTuition = 0 # Initialize four years’ worth of tuition

# Compute tuition in 10 years and total cost of four year's worth of tuition 
while count < 14:
    tuition +=  tuition * PERCENTAGE_INCREASE
    count += 1
    if count == 10:
        print("The tuition in 10 years: $" + str(format(tuition, ".2f")))
    elif count > 10:
        fourYearTuition += tuition
print("The total cost of four year's worth of tuition starting 10 years from now: $" 
      + str(format(fourYearTuition, ".2f")))
    
