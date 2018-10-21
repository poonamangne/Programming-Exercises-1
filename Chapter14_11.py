# 14.11 Write a program that prompts the user to enter a text filename and
# displays the number of vowels and consonants in the file.

# Use a set to store the vowels A, E, I, O, and U.


def main():

    while True:
        try:
            fileName = input("Enter a filename: ").strip()
            infile = open(fileName, "r")
            break
        except IOError:
            print("File " + fileName + " does not exist. Try again")

    try:
        numberOfVowels = 0
        numberOfConsonants = 0
        vowels = {"A", "E", "I", "O", "U"}

        line = infile.read()

        for i in range (0, len(line)):
            if line[i].upper() in vowels:
                numberOfVowels += 1
            elif line[i].isalpha():
                numberOfConsonants += 1

        print("Number of vowels:", numberOfVowels)
        print("Number of consonants:", numberOfConsonants)

    except Exception:
        print("Error!")

    finally:
        infile.close()


main()
