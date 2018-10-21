# 1.18 Write a program that draws a star

import turtle # Import turtle module

turtle.penup()
turtle.goto(0, 100) # Move the turtle to a specific point to position star
turtle.right(72) # Turn right to 72 degrees after subtracting inner angle 36 degrees from 90 degrees
turtle.pendown()

turtle.forward(200) # Draw a side for the star with length 200 pixels
turtle.right(144) # Turn right to 144 degrees after subtracting inner angle 36 degrees from 180 degrees

turtle.forward(200) # Draw a side for the star with length 200 pixels
turtle.right(144) # Turn right to 144 degrees after subtracting inner angle 36 degrees from 180 degrees

turtle.forward(200) # Draw a side for the star with length 200 pixels
turtle.right(144) # Turn right to 144 degrees after subtracting inner angle 36 degrees from 180 degrees

turtle.forward(200) # Draw a side for the star with length 200 pixels
turtle.right(144) # Turn right to 144 degrees after subtracting inner angle 36 degrees from 180 degrees

turtle.forward(200) # Draw a side for the star with length 200 pixels

turtle.done()
