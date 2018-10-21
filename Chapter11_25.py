# 11.25 Write a test program that prompts the user to enter a matrix of numbers and
# tests whether it is a Markov matrix.
# Sample Input [0.15 0.875 0.375], [0.55 0.005 0.225], [0.30 0.12 0.4]
# Sample Input [0.95 -0.875 0.375] [0.65 0.005 0.225] [0.30 0.22 -0.4]

# Check whether a matrix is a Markov matrix
def isMarkovMatrix(m):
    for column in range(0, len(m)):
        sum = 0
        for row in range(0, len(m)):
            if m[row][column] < 0:
                return "It is not a Markov matrix"
            else:
                sum += m[row][column]
        if sum != 1:
            return "It is not a Markov matrix"
        else:
            continue
    return "It is a Markov matrix"

def main():
    
    matrix = []
    
    # n by n matrix
    n = 3
    
    print("Enter a 3-by-3 matrix row by row: ")
    
    # Read numbers as a string from the console
    for row in range(n):
        # Read numbers as a string from the console
        s = input().split() # Extract items from the string
        column = [float(x) for x in s] # Convert items to numbers
        matrix.append(column) # Add columns to the row  
   
    print(isMarkovMatrix(matrix))


main()