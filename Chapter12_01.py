# 12.1 Write a test program that prompts the user to enter the three sides of the triangle,
# a color, and 1 or 0 to indicate whether the triangle is filled
# Sample Input [10, 9, 8]

from GeometricObject import GeometricObject


class Triangle(GeometricObject):

    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def setSide1(self, side1):
        self.__side1 = side1

    def getSide2(self):
        return self.__side2

    def setSide2(self, side2):
        self.__side2 = side2

    def getSide3(self):
        return self.__side3

    def setSide3(self, side3):
        self.__side3 = side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = (s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3)) ** 0.5
        return area

    def getPerimeter(self):
        return self.getSide1() + self.getSide2() + self.getSide3()

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + \
            " side3 = " + str(self.__side3)


def main():

    # Prompt user for inputs
    side1, side2, side3 = eval(input("Enter the three sides of the triangle: "))
    color = input("Enter a color: ")
    filled = eval(input("Is the triangle filled? Enter 1 or 0: "))

    t1 = Triangle(side1, side2, side3)

    t1.setColor(color)
    t1.setFilled(bool(filled))

    # Display Area, Perimeter, color, is filled for the triangle
    print()
    print("Area of the Triangle:", format(t1.getArea(), ".2f"))
    print("Perimeter of the Triangle:", t1.getPerimeter())
    print("Triangle color:", t1.getColor(), "and filled:", t1.isFilled())


main()  # Call the main function
