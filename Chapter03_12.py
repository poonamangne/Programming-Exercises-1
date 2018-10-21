# 3.12 Write a program that prompts the user to enter the length of the star and draw a star

import turtle # Import turtle module

# Prompt the user for length of the star
length = eval(input("Enter the length of the star: "))

turtle.penup()
turtle.goto(0, length / 2) # Move the turtle to a specific point to position star
turtle.right(72) # Turn right to 72 degrees after subtracting inner angle 36 degrees from 90 degrees
turtle.pendown()

turtle.forward(length) # Draw a side for the star with length entered by user
turtle.right(144) # Turn right to 144 degrees after subtracting inner angle 36 degrees from 180 degrees

turtle.forward(length) # Draw a side for the star
turtle.right(144) # Turn right to 144 degrees after subtracting inner angle 36 degrees from 180 degrees

turtle.forward(length) # Draw a side for the star
turtle.right(144) # Turn right to 144 degrees after subtracting inner angle 36 degrees from 180 degrees

turtle.forward(length) # Draw a side for the star
turtle.right(144) # Turn right to 144 degrees after subtracting inner angle 36 degrees from 180 degrees

turtle.forward(length) # Draw a side for the star

turtle.hideturtle() # Make the turtle invisible

turtle.done()