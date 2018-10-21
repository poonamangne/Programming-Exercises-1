# 15.24 Write a program that prompts the user to enter a directory
# and displays the number of files in the directory.

import os


def main():

    path = input("Enter a directory: ").strip()

    try:
        print(getNumberOfFiles(path) , "files in the directory")
    except:
        print("Directory or file does not exist")


def getNumberOfFiles(path):
    count = 0
    lst = os.listdir(path)
    for item in lst:
        newPath = path + "/" + item
        if not os.path.isfile(newPath):
            count += getNumberOfFiles(newPath)
        else:
            count += 1
    return count


main()