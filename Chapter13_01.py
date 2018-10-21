# 13.1 Write a program that removes all the occurrences of a specified string from a text file.
# Sample Input [test1.txt]


def main():

    while True:
        try:
            fileName = input("Enter a filename: ").strip()
            infile = open(fileName, "r")
            break
        except IOError:
            print("File " + fileName + " does not exist. Try again")

    try:
        s = input("Enter the string to be removed: ")

        line = infile.read()
        s1 = line.replace(s, '')

        outfile = open(fileName, "w")
        outfile.write(s1)

        print("Done")

    except Exception:
        print("Error!")

    finally:
        infile.close()
        outfile.close()


main()
