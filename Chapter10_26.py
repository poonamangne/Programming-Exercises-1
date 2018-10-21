# 10.26 Write a test program that prompts the user to enter two sorted lists and
# displays the merged list
# Sample Inputs [1 5 16 61 111], [2 4 5 6]


def merge(list1, list2):
    list3 = []
    while len(list1) and len(list2):
        if list1[0] > list2[0]:
            list3.append(list2.pop(0))
        else:
            list3.append(list1.pop(0))
    if len(list1):
        while len(list1):
            list3.append(list1.pop(0))
    elif len(list2):
        while len(list2):
            list3.append(list2.pop(0))

    for i in list3:
        print(i, end = " ")


def main():

    # Read numbers as a string from the console
    s1 = input("Enter list1: ")
    items = s1.split()  # Extract items from the string
    myList1 = [eval(x) for x in items]  # Convert items to numbers

    # Read numbers as a string from the console
    s2 = input("Enter list2: ")
    items = s2.split()  # Extract items from the string
    myList2 = [eval(x) for x in items]  # Convert items to numbers

    # Display the merged list
    print("The merged list is", end = " ")
    merge(myList1, myList2)


main()  # Call the main function
