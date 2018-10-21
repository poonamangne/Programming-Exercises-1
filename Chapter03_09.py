# 3.9 Write a program that reads the following information and prints a payroll statement

# Prompt the user to enter employee name
employeeName = input("Enter employee's name: ")

# Prompt the user to enter the number of hours worked in a week
numberOfHoursWorked = eval(input("Enter number of hours worked in a week: "))

# Prompt the user to enter the hourly pay rate
hourlyPayRate = eval(input("Enter hourly pay rate: "))

# Prompt the user to enter the federal tax withholding rate
federalTaxWithholdingRate = eval(input("Enter federal tax withholding rate: "))

# Prompt the user to enter the state tax withholding rate
stateTaxWithholdingRate = eval(input("Enter state tax withholding rate: "))

# Compute gross pay
grossPay = hourlyPayRate * numberOfHoursWorked

# Compute federal tax withholding
federalTaxWithholding = federalTaxWithholdingRate * grossPay

# Compute state tax withholding
stateTaxWithholding = stateTaxWithholdingRate * grossPay

# Compute total deduction
totalDeduction = federalTaxWithholding + stateTaxWithholding

# Compute net pay
netPay = grossPay - totalDeduction

# Print the payroll statement
print()
print("Employee Name:", employeeName)
print("Hours worked:", numberOfHoursWorked)
print("Pay Rate: $" + str(hourlyPayRate))
print("Gross Pay: $" + str(grossPay))
print("Deductions:")
print(format("Federal Withholding (", ">22s") + format(federalTaxWithholdingRate, ".1%") 
      + "): $" + format(federalTaxWithholding,".2f"))
print(format("State Withholding (", ">20s") + format(stateTaxWithholdingRate, ".1%") 
      + "): $" + format(stateTaxWithholding,".2f"))
print(format("Total Deduction: $", ">19s") + format(totalDeduction,".2f"))
print("Net Pay: $" + format(netPay,".2f"))
