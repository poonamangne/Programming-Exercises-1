# 11.10 Write a program that randomly fills in 0s and 1s into a matrix, prints the matrix,
# and finds the rows and columns with the most 1s.

import random


# Create a matrix of random 0 and 1
def createMatrix(n):
    m = [[0] * n for i in range(n)]
    for row in range(len(m)):
        for column in range(len(m[row])):
            m[row][column] = random.choice([0, 1])
    return m


# Display rows with most 1's
def countMostOneRows(m):
    n = []
    max1 = 0
    for row in range(len(m)):
        countOne = m[row].count(1)
        n.append(countOne)
        max1 = max(countOne, max1)
    for i in range(len(n)):
        if max1 == n[i]:
            print(i + 1, end = " ")


# Display columns with most 1's
def countMostOneColumns(m):
    n = []
    max1 = 0
    for column in range(len(m)):
        countOne = 0
        for row in range(len(m)):
            if m[row][column] == 1:
                countOne += 1
        n.append(countOne)
        max1 = max(countOne, max1)
    for j in range(len(n)):
        if max1 == n[j]:
            print(j + 1, end = " ")


# Print a matrix
def printMatrix(m):
    for row in range(len(m)):
        for column in range(len(m[row])):
            print(round(m[row][column], 1), end = " ")
        print()
    print()


def main():
    # n by n matrix
    n = 4

    a = createMatrix(n)  # Create a n by n matrix
    printMatrix(a)

    print("The largest row index: ", end = "")
    countMostOneRows(a)
    print()

    print("The largest column index: ", end = "")
    countMostOneColumns(a)


main()
