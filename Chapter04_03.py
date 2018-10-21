# 4.3 Write a program that prompts the user to enter a, b, c, d, e, and f
# and display the result. If ad – bc is 0, report that the equation has no solution

# Prompt the user to enter a, b, c, d, e, and f
a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f:"))

# Compute ad - bc and proceed accordingly
if (a * d - b * c) == 0:
    print("The equation has no solution")
else:
    x = (e * d - b * f) / (a * d - b * c)
    y = (a * f - e * c) / (a * d - b * c)
    print("x is", format(x, ".1f"), "and y is", format(y, ".1f"))
