# 4.39 Write a program that prompts the user to enter the center coordinates and radii of two circles 
# and determines whether the second circle is inside the first or overlaps with the first

import math # Import math module
import turtle # Import turtle module

# Prompt user to enter x, y coordinates & radius of circle1
x1, y1, radius1 = eval(input("Enter circle1's center x-, y-coordinates, and radius:"))

# Prompt user to enter x, y coordinates & radius of circle2
x2, y2, radius2 = eval(input("Enter circle2's center x-, y-coordinates, and radius:"))

# Draw circle 1
turtle.penup()
turtle.goto(x1, y1 - radius1)
turtle.pendown()
turtle.circle(radius1)

# Draw circle 2
turtle.penup()
turtle.goto(x2, y2 - radius2)
turtle.pendown()
turtle.circle(radius2)

# Compute distance between the two centers
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check the positions and display the result
if distance <= abs(radius1 - radius2) and radius1 > radius2:
    turtle.write("circle2 is inside circle1")
elif distance <= abs(radius1 + radius2) and radius1 > radius2:
    turtle.write("circle2 overlaps circle1")
else:
    turtle.write("circle2 does not overlap circle1")
    
turtle.hideturtle() # Make the turtle invisible

turtle.done()