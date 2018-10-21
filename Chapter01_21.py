# 1.21 Write a program that displays a clock to show the time 9:15:00

import turtle # Import turtle module

# Move the turtle to a specific point to position the circle and draw a circle with radius 100
turtle.penup()
turtle.goto(0, -100) 
turtle.pendown()
turtle.circle(100)

# Display the clock hour 3
turtle.penup()
turtle.goto(90, 0)
turtle.pendown()
turtle.write("3") 

# Write the clock hour 12
turtle.penup()
turtle.goto(0, 85)
turtle.pendown()
turtle.write("12") 

# Display the clock hour 9
turtle.penup()
turtle.goto(-90, 0)
turtle.pendown()
turtle.write("9") 

# Display the clock hour 6
turtle.penup()
turtle.goto(0, -95)
turtle.pendown()
turtle.write("6") 

# Draw the clock minute hand
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("gray70") 
turtle.forward(60)

# Draw the clock second hand
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.left(90)
turtle.color("gray30")
turtle.forward(70)

# Draw the clock hour hand
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.left(90)
turtle.color("gray90")
turtle.forward(50)

# Display the clock time
turtle.penup()
turtle.goto(-10, -115)
turtle.color("black")
turtle.write("9:15:00") 

turtle.done()