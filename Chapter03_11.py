# 3.11 Write a program that prompts the user to enter a four-digit integer 
# and displays the number in reverse order

# Prompt the user to enter a number
number = eval(input("Enter an integer: "))

# Compute units digit and remainder number
unitsDigit = number % 10
remainderNumber = number // 10

# Compute tens digit and remainder number
tensDigit = remainderNumber % 10
remainderNumber = remainderNumber // 10

# Compute hundreds digit and remainder number
hundredsDigit = remainderNumber % 10
remainderNumber = remainderNumber // 10

# Compute the reversed number
reversedNumber = unitsDigit * 1000 + tensDigit * 100 + hundredsDigit * 10 + remainderNumber

# Display result
print("The reversed number is", reversedNumber)