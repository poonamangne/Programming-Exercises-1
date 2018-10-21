# 6.41 Write a program that displays a rectangle centered at (-75, 0) with width and height 100 
# and a circle centered at (50, 0) with radius 50. Fill 10 random points inside the rectangle 
# and 10 inside the circle

import turtle # Import turtle module
import random # Import random module

# Draw a point at the specified location (x, y)
def drawPoint(x, y):
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.begin_fill() # Begin to fill color in a shape
    turtle.circle(3)
    turtle.end_fill() # Fill the shape

# Draw a circle centered at (x, y) with the specified radius
def drawCircle(x = 0, y = 0, radius = 10):
    turtle.penup() # Pull the pen up
    turtle.goto(x, y - radius)
    turtle.pendown() # Pull the pen down
    turtle.circle(radius)

# Draw a rectangle at (x, y) with the specified width and height
def drawRectangle(x = 0, y = 0, width = 10, height = 10):
    turtle.penup() # Pull the pen up
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown() # Pull the pen down
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    
# Generate a random point (a,b) with range x1 < a < x2 and y1 < b < y2   
def randomPoint(x1, x2, y1, y2):
    a = random.randint(x1, x2)
    b = random.randint(y1, y2)
    return a, b

# Draw n random points inside the rectangle   
def drawPointsInsideRectangle(n, x, y, width, height):
    while n > 0:
        a, b = randomPoint(x - width / 2, x + width / 2, y - height / 2, y + height / 2) 
        if (x - width / 2 + 3) < a < (x + width / 2 - 3) \
        and (y - height / 2) < b + 6 < (y + height / 2): # Adjustment for point circle of radius 3
            drawPoint(a, b)
            n -= 1
        
# Draw n random points inside the circle  
def drawPointsInsideCircle(n, x, y, radius):
    while n > 0:
        a, b = randomPoint(x - radius, x + radius, y - radius, y + radius) 
        if computeDistance(a, b + 3, x, y) + 3 < radius: # Adjustment for point circle of radius 3
            drawPoint(a, b)
            n -= 1

# Compute the distance between two points (x1, y1) and (x2, y2)
def computeDistance(x1, y1, x2, y2):   
    distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5  
    return distance
                      
# Draw a rectangle centered at (-75, 0) with width and height 100
drawRectangle(-75, 0, 100, 100)

# Draw a circle centered at (50, 0) with radius 50
drawCircle(50, 0, 50)

# Draw 10 random points inside the rectangle centered at (-75, 0) with width and height 100
drawPointsInsideRectangle(10, -75, 0, 100, 100)

# Draw 10 random points inside the circle centered at (50, 0) with radius 50
drawPointsInsideCircle(10, 50, 0, 50)

turtle.hideturtle() # Make the turtle invisible

turtle.done()