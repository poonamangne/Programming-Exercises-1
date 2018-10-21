# 12.2 Write a test program that prompts the user to enter a two-dimensional list and
# displays the location of the largest element in the list.
# Sample Input [23.5 35 2 10] [4.5 3 45 3.5] [35 44 5.5 12.6]


class Location:

    def __init__(self, row = 0, column = 0, maxValue = 0):
        self.__row = row
        self.__column = column
        self.__maxValue = maxValue

    def getRow(self):
        return self.__row

    def setRow(self, row):
        self.__row = row

    def getColumn(self):
        return self.__column

    def setColumn(self, column):
        self.__column = column

    def getMaxValue(self):
        return self.__maxValue

    def setMaxValue(self, maxValue):
        self.__maxValue = maxValue


# Returns the location of the largest element in a two-dimensional list
def locateLargest(a):
    l1 = Location()
    indexOfRow, indexOfColumn, maxElement = 0, 0, 0
    for row in range(len(a)):
        for column in range(len(a[row])):
            if a[row][column] > maxElement:
                maxElement = a[row][column]
                indexOfRow = row
                indexOfColumn = column
    l1.setRow(indexOfRow)
    l1.setColumn(indexOfColumn)
    l1.setMaxValue(maxElement)
    return l1


def main():
    rows, columns = eval(input("Enter the number of rows and columns in the list: "))

    matrix = []

    # Read numbers as a string from the console
    for row in range(rows):
        # Read numbers as a string from the console
        print("Enter row " + str(row) + ":" , end = " ")
        s = input().split()  # Extract items from the string
        column = [eval(x) for x in s]  # Convert items to numbers
        matrix.append(column)  # Add columns to the row

    l2 = locateLargest(matrix)
    print("The location of the largest element " + str(l2.getMaxValue()) + " is at (" + str(l2.getRow()) \
          +", " + str(l2.getColumn()) + ")")


main()
