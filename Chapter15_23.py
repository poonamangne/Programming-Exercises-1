# 15.23 Write a test program that prompts the user to enter a string
# and displays all its permutations


def displayPermutation(s):
    displayPermutationHelper("", s)


def displayPermutationHelper(s1, s2):
    if len(s2) == 0:
        print(s1)
    else:
        for i in range(len(s2)):
            displayPermutationHelper(s1 + s2[i], s2[ : i] + s2[i + 1 : ])


def main():
    s = input("Enter a string: ").strip()
    displayPermutation(s)


main()
