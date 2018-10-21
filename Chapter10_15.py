# 10.15 Write a test program that prompts the user to enter a list and displays 
# whether the list is sorted or not
# Sample Inputs [1 1 3 4 4 5 7 9 10 30 11], [1 1 3 4 4 5 7 9 10 30]

# Create a list
def createList():
    # Read numbers as a string from the console
    s = input("Enter numbers: ")
    items = s.split() # Extract items from the string
    myList = [eval(x) for x in items] # Convert items to numbers
    return myList # Return the list

# Check if list is already sorted in increasing order
def isSorted(lst):
    myList = lst.copy() # Make a copy of the list for comparison
    lst.sort() # Sort the list
    if myList == lst: # Return true if already sorted
        return True
    else:
        return False
    
def displayResult(myList):
    if isSorted(myList):
        return "The list is sorted"
    else:
        return "The list is not sorted"
    
def main():
    # Create a list of integers
    myList = createList()
    
    # Display the result
    print(displayResult(myList))
 


main() # Call the main function  