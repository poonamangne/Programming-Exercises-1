# 11.51 Write a program that prompts the user to enter the students’ names and 
# their scores on one line, and prints student names in increasing order of their scores.
# Sample Input [John 34 Jim 45 Peter 59 Tim 45]

# Create a list
def createList(s):
    myList = []
    i = 0
    for row in range(0, int(len(s) / 2)):
        myList.append([])
        myList[row].append(eval(s[i + 1]))
        myList[row].append(s[i])
        i += 2
    return myList

# Print the list
def printList(myList):
    for row in range(0, len(myList)):
        for column in range(len(myList[row]) - 1, -1, -1):
            print(format(str(myList[row][column]), "<6s"), end = " ")
        print()

def main():
   
    print("Enter students’ names and scores: ")
    
    # Read a string from the console
    s = input().split() # Extract items from the string
    
    studentList = createList(s)
    
    studentList.sort() # Sort the list
    
    printList(studentList)
    

main()