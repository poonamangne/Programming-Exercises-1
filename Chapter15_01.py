# 15.1 Write a recursive function that computes the sum of the digits in an integer


def sumDigits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sumDigits(n // 10)


def main():
    number = eval(input("Enter a number: "))
    print("The sum of the digits is", sumDigits(number))


main()
