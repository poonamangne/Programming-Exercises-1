# 11.36 Write a Turtle program that displays a random path that starts from the center and ends at
# a point on the boundary, or ends at a dead-end point

import turtle
import random

# Draw 16 by 16 lattice
def drawLattice(n, m):
    turtle.color("gray") # Color for lattice
    x = -n
    for y in range(-n, n + 1, m):
        turtle.penup()
        turtle.goto(x, y) # Draw a horizontal line
        turtle.pendown()
        turtle.forward(2 * n)   
    y = n
    turtle.right(90)
    for x in range(-n, n + 1, m):
        turtle.penup()
        turtle.goto(x, y) # Draw a vertical line
        turtle.pendown()
        turtle.forward(2 * n)

# Create a random point
def createPoint(x, y, n):
    r = random.choice([0, 1, 2, 3])
    if r == 0:
        x += n # Walk right
    elif r == 1:
        y -= n # Walk down
    elif r == 2:
        x -= n # Walk left
    else:    
        y += n # Walk up
    return x, y, r

# Check if point is new            
def isNewPoint(x, y, m):
    for row in range(0, len(m)):
        if (x == m[row][0]) and (y == m[row][1]):
            return False
    return True

def main():
    n = 160
    m = 20
    
    drawLattice(n, m)
    
    turtle.pensize(2)
    turtle.color("red")
    
    x, y = 0, 0
    matrix = [[x, y]]
    
    turtle.penup()
    turtle.goto(x, y) # Go to the center
    turtle.pendown()
    
    while abs(x) < n and abs(y) < n:
        x1, y1, r = createPoint(x, y, m)
        if isNewPoint(x1, y1, matrix):
            if r == 0:
                turtle.setheading(0)
            elif r == 1:
                turtle.setheading(270)
            elif r == 2:
                turtle.setheading(180)
            elif r == 3:
                turtle.setheading(90)
            turtle.forward(m)
            matrix.append([x1, y1])
            x, y = x1, y1
    
    turtle.hideturtle()
    turtle.done()
    
    
main()