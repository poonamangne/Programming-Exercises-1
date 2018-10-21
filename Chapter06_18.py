# 6.18 Write a function that displays an n-by-n matrix

import random # Import random module

# Display a n-by-n matrix
def printMatrix(n):
    for i in range(0, n):
        for j in range(0, n):
            print(random.randint(0, 1), end = " ")
        print() # Move to new line
    
def main():
    n = eval(input("Enter n: ")) # Prompt the user to enter n
    printMatrix(n)
    
main() # Call the main function