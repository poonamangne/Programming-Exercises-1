# Write a test program that prompts the user to enter a, b, c, d, e, and f and displays the result.
# If ad - bc is 0, report that “The equation has no solution.”
# Sample Inputs [9.0, 4.0, 3.0, -5.0, -6.0, -21.0] , [1.0, 2.0, 2.0, 4.0, 4.0, 5.0]


class LinearEquation:

    # Construct a LinearEquation object
    def __init__(self, a = 0, b = 0, c = 0, d = 0, e = 0, f = 0):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def isSolvable(self):
        a = self.getA()
        b = self.getB()
        c = self.getC()
        d = self.getD()
        if (a * d - b * c) != 0:
            return True
        else:
            return False

    def solution(self):
        if self.isSolvable():
            a = self.getA()
            b = self.getB()
            c = self.getC()
            d = self.getD()
            e = self.getE()
            f = self.getF()
            self.__x = (e * d - b * f) / (a * d - b * c)
            self.__y = (a * f - e * c) / (a * d - b * c)
            return self.getX(), self.getY()
        else:
            return "The equation has no solution."


def main():
    # Prompt the user to enter a, b, c, d, e, and f
    a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f: "))

    # Create a LinearEquation object
    e1 = LinearEquation(a, b, c, d, e, f)

    # Display result
    print(e1.solution())

# main() # Call the main function

