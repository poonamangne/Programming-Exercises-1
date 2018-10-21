# 5.55 Write a program to draw a chessboard

import turtle  # Import turtle module

sizeOfSquare = 50  # Initialize size of each square

# Compute start and end range for the outer square
startRange = -(sizeOfSquare * 4)
endRange = sizeOfSquare * 4

# Draw the chessboard
for x in range(startRange, endRange, sizeOfSquare):
    for y in range(startRange, endRange, sizeOfSquare):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        # if the square has both even x, y coordinates or both odd x, y coordinates,
        # it will be filled with color
        if (abs(x / sizeOfSquare) % 2 == 0 and abs(y / sizeOfSquare) % 2 == 0) \
        or (abs(x / sizeOfSquare) % 2 != 0 and abs(y / sizeOfSquare) % 2 != 0):
            turtle.begin_fill()  # Begin to fill color in the square
            for i in range(0, 4):
                turtle.left(90)
                turtle.forward(sizeOfSquare)
            turtle.end_fill()
        else:
            for i in range(0, 4):
                turtle.left(90)
                turtle.forward(sizeOfSquare)

turtle.hideturtle()  # Makes the turtle invisible

turtle.done()
