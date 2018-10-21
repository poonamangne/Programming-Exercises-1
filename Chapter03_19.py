# 3.19 Write a program that prompts the user to enter two points 
# and draw a line to connect the points and displays the coordinates of the point

import turtle # Import turtle module

# Prompt the user for point 1
x1, y1 = eval(input("Enter x1 and y1 for point 1: "))

# Prompt the user for point 2
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))

# Display the two points and the connecting line
turtle.penup()
turtle.goto(x1, y1) # Move to (x1, y1)
turtle.pendown()
turtle.write("(" + str(x1) + ", " + str(y1) + ")") # Display the coordinates of point 1
turtle.goto(x2, y2) # Draw a line to connect both points
turtle.write("(" + str(x2) + ", " + str(y2) + ")") # Display the coordinates of point 2

turtle.hideturtle() # Makes the turtle invisible

turtle.done()