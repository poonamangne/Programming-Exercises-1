# 3.6 Write a program that draws a triangle, square, pentagon, hexagon, and octagon

import turtle # Import turtle module

# Draw a triangle with bottom side parallel to x-axis
turtle.setheading(60) # Set the turtle’s heading to 60 degrees 
turtle.pensize(3) # Set pen thickness to 3 pixels
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in the shape
turtle.color("red")
turtle.circle(40, steps = 3) # Draw a triangle
turtle.end_fill() # Fill the shape

# Draw a square with bottom side parallel to x-axis
turtle.setheading(45) # Set the turtle’s heading to 45 degrees
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in the shape
turtle.color("blue")
turtle.circle(40, steps = 4) # Draw a square 
turtle.end_fill() # Fill the shape

# Draw a pentagon with bottom side parallel to x-axis
turtle.setheading(36) # Set the turtle’s heading to 36 degrees
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in the shape
turtle.color("green")
turtle.circle(40, steps = 5) # Draw a pentagon 
turtle.end_fill() # Fill the shape

# Draw a hexagon with bottom side parallel to x-axis
turtle.setheading(30) # Set the turtle’s heading to 30 degrees
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in the shape
turtle.color("yellow")
turtle.circle(40, steps = 6) # Draw a hexagon 
turtle.end_fill() # Fill the shape

# Draw a octagon with bottom side parallel to x-axis
turtle.setheading(22.5) # Set the turtle’s heading to 22.5 degrees
turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill() # Begin to fill color in the shape
turtle.color("purple")
turtle.circle(40, steps = 8) # Draw a octagon 
turtle.end_fill() # Fill the shape

turtle.hideturtle() # Make the turtle invisible

turtle.done()