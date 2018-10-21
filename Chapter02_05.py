# 2.5 Write a program that reads the subtotal, gratuity rate and computes the gratuity and total
# Sample Inputs [15.69, 15]

# Prompt the user for subtotal and the gratuity rate
subTotal, gratuityRate = eval(input("Enter the subtotal and a gratuity rate: "))

# Compute gratuity amount
gratuityAmount = subTotal * (gratuityRate / 100)

# Compute total
total = subTotal + gratuityAmount

# Display gratuity amount and total with two digits after decimal point
print("The gratuity is", int(gratuityAmount * 100) / 100.0, \
      "and the total is", int(total * 100) / 100.0)
