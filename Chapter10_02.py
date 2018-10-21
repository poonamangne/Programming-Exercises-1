# 10.2 Write a program that reads a list of integers and displays them in the reverse order
# in which they were read.
# Sample Input [2 5 6 4 3 23 43]


# Create a list of integers
def createList():
    # Read numbers as a string from the console
    s = input("Enter integers: ")
    items = s.split()  # Extract items from the string
    myList = [eval(x) for x in items]  # Convert items to numbers
    return myList  # Return the list


# Display the list of integers in reverse order
def displayReverseList(myList):
    myList.reverse()  # Reverse the list
    for i in myList:
        print(i, end = " ")


def main():
    # Create a list of n integers
    myList = createList()

    # Print the list in reverse order
    print("The list in reverse order:")
    displayReverseList(myList)


main()  # Call the main function
