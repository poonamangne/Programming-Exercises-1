# 15.21 Write a test program that prompts the user to enter a binary string and
# displays its decimal equivalent


def binaryToDecimal(binaryString):
    n = len(binaryString)
    if n == 0:
        return 0
    else:
        return int(binaryString[0]) * (2 ** (n - 1)) + binaryToDecimal(binaryString[1 : n])


def main():
    binaryString = input("Enter a binary number: ")
    print("Decimal:", binaryToDecimal(binaryString))


main()
