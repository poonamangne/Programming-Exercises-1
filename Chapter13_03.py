# 13.3 Write a program that reads the scores from the file and displays their total and average.
# Sample Input [scores.txt]


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

        numberOfScores = 0
        totalScore = 0

        while line != "":
            s1 = line.split()
            numberOfScores += len(s1)
            s2 = [eval(x) for x in s1]
            for number in s2:
                totalScore += number
            line = infile.readline()

        averageScore = totalScore / numberOfScores

        print("There are", numberOfScores, "scores")
        print("The total is", totalScore)
        print("The average is", averageScore)

    except Exception:
        print("Error!")

    finally:
        infile.close()


main()
