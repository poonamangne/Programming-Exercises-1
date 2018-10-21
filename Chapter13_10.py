# 13.10 Modify the Rational class to throw a RuntimeError exception if the denominator is 0


class Rational:

    def __init__(self, numerator = 1, denominator = 0):
        divisor = gcd(numerator, denominator)
        if divisor == 0:
            raise RuntimeError()
        else:
            self.__numerator = (1 if denominator > 0 else -1) * int(numerator / divisor)
            self.__denominator = int(abs(denominator) / divisor)

    # Add a rational number to this rational number
    def __add__(self, secondRational):
        n = self.__numerator * secondRational[1] + self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)

    # Subtract a rational number from this rational number
    def __sub__(self, secondRational):
        n = self.__numerator * secondRational[1] - self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)

    # Multiply a rational number by this rational number
    def __mul__(self, secondRational):
        n = self.__numerator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n, d)

    # Divide a rational number by this rational number
    def __truediv__(self, secondRational):
        n = self.__numerator * secondRational[1]
        d = self.__denominator * secondRational[0]
        return Rational(n, d)

    # Return a float for the rational number
    def __float__(self):
        return self.__numerator / self.__denominator

    # Return an integer for the rational number
    def __int__(self):
        return int(self.__float__())

    # Return a string representation
    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        else:
            return str(self.__numerator) + "/" + str(self.__denominator)

    def __lt__(self, secondRational):
        return self.__cmp__(secondRational) < 0

    def __le__(self, secondRational):
        return self.__cmp__(secondRational) <= 0

    def __gt__(self, secondRational):
        return self.__cmp__(secondRational) > 0

    def __ge__(self, secondRational):
        return self.__cmp__(secondRational) >= 0

    def __cmp__(self, secondRational):
        temp = self.__sub__(secondRational)
        if temp[0] > 0:
            return 1
        elif temp[0] < 0:
            return -1
        else:
            return 0

    # Return numerator and denominator using an index operator
    def __getitem__(self, index):
        if index == 0:
            return self.__numerator
        else:
            return self.__denominator


def gcd(n, d):
    n1 = abs(n)
    n2 = abs(d)
    gcd = 1
    k = 2
    if n2 != 0:
        while k <= n1 and k <= n2:
            if n1 % k == 0 and n2 % k == 0:
                gcd = k
            k += 1
        return gcd
    else:
        return 0


def main():
    # Create and initialize two rational numbers r1 and r2.
    try:
        r1 = Rational(4, 2)
        r2 = Rational(2, 0)

        # Display results
        print(r1, "+", r2, "=", r1 + r2)
        print(r1, "-", r2, "=", r1 - r2)
        print(r1, "*", r2, "=", r1 * r2)
        print(r1, "/", r2, "=", r1 / r2)

        print(r1, ">", r2, "is", r1 > r2)
        print(r1, ">=", r2, "is", r1 >= r2)
        print(r1, "<", r2, "is", r1 < r2)
        print(r1, "<=", r2, "is", r1 <= r2)
        print(r1, "==", r2, "is", r1 == r2)
        print(r1, "!=", r2, "is", r1 != r2)

        print("int(r2) is", int(r2))
        print("float(r2) is", float(r2))

        print("r2[0] is", r2[0])
        print("r2[1] is", r2[1])

    except RuntimeError:
        print("Denominator is zero")


main()
