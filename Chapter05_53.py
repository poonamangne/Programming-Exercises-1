# 5.53 Write a program that plots the sine function in red and cosine in blue

import turtle # Import turtle module
import math # Import math module

# Draw the X-axis
turtle.penup() 
turtle.goto(-200, 0)
turtle.pendown()
turtle.forward(400)

turtle.penup() 
turtle.goto(210, 0)
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

# Display -2Pi and 2Pi 
turtle.color("black")   
turtle.penup() 
turtle.goto(-100, -15)
turtle.pendown()
turtle.write("-2\u03c0")
turtle.penup() 
turtle.goto(100, -15)
turtle.pendown()
turtle.write("2\u03c0")

# Plot the sine function in red
turtle.penup()
for x in range(-175, 176):
    turtle.goto(x, 50 * math.sin((x / 100) * 2 * math.pi))
    turtle.color("red")
    turtle.pendown()

# Plot the cosine function in blue
turtle.penup()
for x in range(-175, 176):
    turtle.goto(x, 50 * math.cos((x / 100) * 2 * math.pi))
    turtle.color("blue")
    turtle.pendown()

turtle.hideturtle() # Makes the turtle invisible

turtle.done()