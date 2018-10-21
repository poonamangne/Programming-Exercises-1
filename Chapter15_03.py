# 15.3 Write a test program that prompts the user to enter two integers
# and displays their GCD


def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


def main():
    m, n = eval(input("Enter two integers: "))
    print("GCD is", gcd(m, n))


main()
