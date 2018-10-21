# 13.2 Write a program that will count the number of characters, words, and lines in a file.


def main():

    while True:
        try:
            fileName = input("Enter a filename: ").strip()
            infile = open(fileName, "r")
            break
        except IOError:
            print("File " + fileName + " does not exist. Try again")
    try:
        line = infile.readline()

        numberOfWords = 0
        numberOfLines = 0
        numberOfCharacters = 0

        while line != "":
            numberOfCharacters += len(line)
            s1 = line.split()
            numberOfWords += len(s1)
            numberOfLines += 1
            line = infile.readline()

        if numberOfCharacters != 1:
            print(numberOfCharacters, "characters")
        else:
            print(numberOfCharacters, "character")
        if numberOfWords != 1:
            print(numberOfWords, "words")
        else:
            print(numberOfWords, "word")
        if numberOfLines != 1:
            print(numberOfLines, "lines")
        else:
            print(numberOfLines, "line")

    except Exception:
        print("Error!")

    finally:
        infile.close()


main()
