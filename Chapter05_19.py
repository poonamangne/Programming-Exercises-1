# 5.19 Write a program that prompts the user to enter an integer from 1 to 15 and displays a pyramid

# Prompt the user for input
n = eval(input("Enter the number of lines from 1-15: "))

for i in range(1, n + 1):
    for j in range(1, n + 1 - i):  # Print empty spaces for each row
        print(" ", end = " ")

    for k in range(i, 0, -1):
        print(k, end = " ")  # Print the numbers in each row in decreasing order from row number to 1

    for l in range(2, i + 1):
        print(l, end = " ")  # Print the numbers in each row in increasing order from 2 to row number

    print()  # Jump to the new line
