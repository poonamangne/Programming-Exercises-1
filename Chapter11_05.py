# 11.5 Write a test program that prompts the user to enter two 3 by 3 matrices and displays their sum.
# Sample Input [1 2 3 4 5 6 7 8 9] [0 2 4 1 4.5 2.2 1.1 4.3 5.2]

# Add two matrices
def addMatrix(a, b):
    n = len(a)
    c = [[0] * n for i in range(n)]
    for row in range(n):
        for column in range(len(a[row])):
            c[row][column] = a[row][column] + b[row][column]
    return c

# Create a matrix
def createMatrix(s, n):
    numbers = [float(x) for x in s] # Convert items to numbers
    m = [[0] * n for i in range(n)]
    j = 0
    for row in range(len(m)):
        for column in range(len(m[row])):
            m[row][column] = numbers[j]
            j += 1
    return m

# Print a matrix
def printMatrix(m):
    for row in range(len(m)):
        for column in range(len(m[row])):
            print(round(m[row][column], 1), end = " ")
        print()
    print()

def main():
    # n by n matrix
    n = 3
    
    # Read numbers as a string from the console and create a matrix of n by n
    s1 = input("Enter matrix1: ").split() # Extract items from the string
    a = createMatrix(s1, n)
    
    s2 = input("Enter matrix2: ").split() # Extract items from the string
    b = createMatrix(s2, n)
    
    print("The matrices are added as follows:")
    c = addMatrix(a, b)
    printMatrix(a)
    print(" + ")
    printMatrix(b)
    print(" = ")
    printMatrix(c)
    
    

main()