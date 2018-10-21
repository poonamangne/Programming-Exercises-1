# 5.54 Write a program that draws a diagram for the function f(x) = x2

import turtle # Import turtle module

# Draw the X-axis
turtle.penup() 
turtle.goto(-100, 0)
turtle.pendown()
turtle.forward(200)

turtle.penup() 
turtle.goto(110, 0)
turtle.write("X")
turtle.pendown()

# Draw the Y-axis
turtle.penup() 
turtle.goto(0, -100)
turtle.left(90)
turtle.pendown()
turtle.forward(200)

turtle.penup() 
turtle.goto(0, 110)
turtle.write("Y")
turtle.pendown()

# Draw the function f(x) = x2
turtle.penup()
for x in range(-15, 15):
    turtle.goto(x, x ** 2)
    turtle.pendown()

turtle.hideturtle() # Makes the turtle invisible

turtle.done()