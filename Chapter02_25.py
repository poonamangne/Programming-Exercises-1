# 2.25 Write a program that prompts the user to enter the center of a rectangle, width, and height, 
# and displays the rectangle

import turtle # Import turtle module

# Prompt the user for center of the rectangle
x, y = eval(input("Enter x and y for center for the rectangle: "))

# Prompt the user for width and height of the rectangle
width, height = eval(input("Enter width, height for rectangle: "))

# Move the turtle to a specific point to position the rectangle with given center
turtle.penup()
turtle.goto(x + (width / 2), y - (height / 2))
turtle.pendown()

# Draw the height of the rectangle
turtle.left(90)
turtle.forward(height)

# Draw the width of the rectangle
turtle.left(90)
turtle.forward(width)

# Draw the height of the rectangle
turtle.left(90)
turtle.forward(height)

# Draw the width of the rectangle
turtle.left(90)
turtle.forward(width)

turtle.done()