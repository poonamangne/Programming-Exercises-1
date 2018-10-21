# 11.13 Write a test program that prompts the user to enter a two dimensional list and
# displays the location of the largest element in the list
# Sample Input [23.5 35 2 10] [4.5 3 45 3.5] [35 44 5.5 11.6]


# Returns the location of the largest element in a two-dimensional list
def locateLargest(a):
    indexOfRow, indexOfColumn, maxElement = 0, 0, 0
    for row in range(len(a)):
        for column in range(len(a[row])):
            if a[row][column] > maxElement:
                maxElement = a[row][column]
                indexOfRow = row
                indexOfColumn = column
    return indexOfRow, indexOfColumn


def main():

    matrix = []

    n = eval(input("Enter the number of rows in the list: "))

    # Read numbers as a string from the console
    for row in range(n):
        # Read numbers as a string from the console
        print("Enter a row:", end = " ")
        s = input().split()  # Extract items from the string
        column = [eval(x) for x in s]  # Convert items to numbers
        matrix.append(column)  # Add columns to the row

    print("The location of the largest element is at", locateLargest(matrix))


main()
