# 10.16 Write a test program that reads in ten numbers, invokes the function, and
# displays the sorted numbers
# Sample Input [6 4 1 0 9 2 8 5 2 1]


# Create a list
def createList():
    # Read numbers as a string from the console
    s = input("Enter numbers: ")
    items = s.split()  # Extract items from the string
    myList = [eval(x) for x in items]  # Convert items to numbers
    return myList  # Return the list


# Sort function using bubble-sort algorithm
def bubbleSort(myList):
    for i in range(0, len(myList)):
        for j in range(0, len(myList) - 1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]


def main():
    # Create a list of integers
    myList = createList()

    # Invoke the bubble sort function
    bubbleSort(myList)

    print(myList)


main()  # Call the main function
