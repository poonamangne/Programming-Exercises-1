# 5.16 Write a program to find the greatest common divisor of two integers

# Prompt the user for two integers
n1, n2 = eval(input("Enter two integers: "))

# Compute d to be the minimum of the two integers
d = min(n1, n2)

# Initialize gcd
gcd = 1

# Check for greatest common divisor
while d > 0:
    if (n1 % d == 0) and (n2 % d == 0):
        gcd = d
        break
    else:
        d -= 1

# Display the greatest common divisor 
print("The greatest common divisor for", n1, "and", n2, "is", gcd)