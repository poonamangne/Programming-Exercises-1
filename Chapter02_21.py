#2 .21 Write a program that prompts the user to enter a monthly saving amount and 
# displays the account value after the sixth month

# Compute monthly interest rate from annual interest rate constant
ANNUAL_INTEREST_RATE = 0.05
monthlyInterestRate = ANNUAL_INTEREST_RATE / 12

# Prompt the user to enter a monthly saving amount
monthlySavingAmount = eval(input("Enter the monthly saving amount: "))

# Constant 
NUMBER_OF_MONTHS = 6

# Compute account value after first month
accountBalance = monthlySavingAmount * (1 + monthlyInterestRate)

# Compute account value after second month
accountBalance = (accountBalance + monthlySavingAmount) * (1 + monthlyInterestRate)

# Compute account value after third month
accountBalance = (accountBalance + monthlySavingAmount) * (1 + monthlyInterestRate)

# Compute account value after fourth month
accountBalance = (accountBalance + monthlySavingAmount) * (1 + monthlyInterestRate)

# Compute account value after fifth month
accountBalance = (accountBalance + monthlySavingAmount) * (1 + monthlyInterestRate)

# Compute account value after sixth month
accountBalance = (accountBalance + monthlySavingAmount) * (1 + monthlyInterestRate)

# Display the account value after the sixth month with two digits after decimal point
print("After", NUMBER_OF_MONTHS, "months, the account value is", int(accountBalance * 100) / 100.0)