# 11.2 Write a test program that reads a 4 by 4 matrix and displays 
# the sum of all its elements on the major diagonal
# Sample Input [1 2 3 4] [5 6.5 7 8] [9 10 11 12] [13 14 15 16]

# Sums all the numbers of the major diagonal in an n by n matrix of integers
def sumMajorDiagonal(m):
    sum = 0
    for row in range(len(m)):
        for column in range(len(m[row])):
            if row == column:
                sum += m[row][column]
    return sum

def main():
    
    matrix = [] # Create an empty list
    
    # n by n matrix
    n = 4
    
    # Read numbers as a string from the console
    for row in range(n):
        # Read numbers as a string from the console
        print("Enter a 4-by-4 matrix row for row " + str(row + 1) + ":", end =" ")
        s = input().split() # Extract items from the string
        column = [eval(x) for x in s] # Convert items to numbers
        matrix.append(column) # Add columns to the row
    print("Sum of the elements in the major diagonal is", sumMajorDiagonal(matrix))
    

main()