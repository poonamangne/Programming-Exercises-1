# 2.6 Write a program that reads an integer between 0 and 1000 and adds all the digits in the integer

# Prompt the user to enter a number
number = eval(input("Enter a number between 0 and 1000: "))

# Get units digit
unitsDigit = number % 10

# Get tens digit
tensDigit = (number // 10) % 10

# Get hundred's digit
hundredsDigit = (number // 100) % 10

# Compute sum of the digits
sumOfDigits = unitsDigit + tensDigit + hundredsDigit

# Display result
print("The sum of the digits is", sumOfDigits)
