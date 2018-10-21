# 2.14 Write a program that prompts the user to enter the three points (x1, y1), (x2, y2), and (x3, y3)
# of a triangle and displays its area
# Sample Inputs [1.5, -3.4, 4.6, 5, 9.5, -3.4]

# Prompt the user to enter three points of a triangle
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))

# Compute the sides of the triangle
side1 = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
side2 = ((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3)) ** 0.5
side3 = ((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3)) ** 0.5

# Compute the area of a triangle
s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    
# Display result with one digit after decimal point
print("The area of the triangle is", int(area * 10) / 10.0)