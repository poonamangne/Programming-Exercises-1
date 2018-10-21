# 10.3 Write a program that reads some integers between 1 and 100 and counts the occurrences of each.
# Sample Input [2 5 6 5 4 3 23 43 2]

# Create a list of integers
def createList():
    # Read numbers as a string from the console
    s = input("Enter integers between 1 and 100 separated by spaces in one line: ")
    items = s.split() # Extract items from the string
    myList = [eval(x) for x in items] # Convert items to numbers
    return myList # Return the list

# Display the list of integers
def countOccurrences(myList):
    myList.sort() # Sort list in ascending order
    i = 0
    while i < len(myList):
        count = myList.count(myList[i])
        if count > 1:
            print(myList[i], "occurs", count, "times")
        else:
            print(myList[i], "occurs", count, "time")
        i += count
        count = 0

def main():
    # Create a list of n integers between 1 and 100
    myList = createList()
   
    # Count the occurrence of each integer in the list
    countOccurrences(myList)
 


main() # Call the main function  