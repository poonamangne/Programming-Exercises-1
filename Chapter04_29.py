# 4.29 Write a program that prompts the user to enter the center coordinates and radii of two circles 
# and determines whether the second circle is inside the first or overlaps with the first

import math # Import math module

# Prompt user to enter x, y coordinates & radius of circle1
x1, y1, radius1 = eval(input("Enter circle1's center x-, y-coordinates, and radius:"))

# Prompt user to enter x, y coordinates & radius of circle2
x2, y2, radius2 = eval(input("Enter circle2's center x-, y-coordinates, and radius:"))

# Compute distance between the two centers
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check the positions and display the result
if distance <= abs(radius1 - radius2) and radius1 > radius2:
    print("circle2 is inside circle1")
elif distance <= abs(radius1 + radius2) and radius1 > radius2:
    print("circle2 overlaps circle1")
else:
    print("circle2 does not overlap circle1")