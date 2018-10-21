# 7.9 Write a program that prompts the user to enter four endpoints and displays the intersecting point
# Sample Inputs [2.0, 2.0, 0, 0] , [0, 2.0, 2.0, 0]

from Chapter07_07 import LinearEquation

def main():
    # Prompts the user to enter four endpoints
    x1, y1, x2, y2 = eval(input("Enter the endpoints of the first line segment: "))
    x3, y3, x4, y4 = eval(input("Enter the endpoints of the second line segment: "))
    
    # Calculate the value of a, b, e using the slope point form for an equation y - y1 = m * (x - x1) 
    # and m = (y2 - y1) / (x2 - x1) and comparing with ax + by = e
    a = y2 - y1
    b = -(x2 - x1)
    e = x1 * (y2 - y1) - y1 * (x2 - x1) 
    
    # Calculate the value of c, d, f using the slope point form for an equation y - y1 = m * (x - x1) 
    # and m = (y2 - y1) / (x2 - x1) and comparing with cx + dy = f
    c = y4 - y3
    d = -(x4 - x3)
    f = x3 * (y4 - y3) - y3 * (x4 - x3)
    
    # Create a LinearEquation object and display the intersecting point
    e1 = LinearEquation(a, b, c, d, e, f)
    print("The intersecting point is:", e1.solution())
    
    
    
main() # Call the main function