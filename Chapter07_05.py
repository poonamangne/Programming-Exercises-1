# 7.5 Write a test program that creates 3 RegularPolygon objects. For each object, 
# display its perimeter and area.

import math # Import math module

class RegularPolygon:
    # Construct a RegularPolygon object with default values
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
        
    def getN(self):
        return self.__n
    
    def setN(self, n):
        self.__n = n
        
    def getSide(self):
        return self.__side
    
    def setSide(self, side):
        self.__side = side
        
    def getX(self):
        return self.__x
    
    def setX(self, x):
        self.__x = x
        
    def getY(self):
        return self.__y
    
    def setY(self, y):
        self.__y = y
        
    def getPerimeter(self):
        return self.getN() * self.getSide()
    
    def getArea(self):
        n = self.getN()
        side = self.getSide()
        area = (n * side * side) / (4 * math.tan(math.pi / n))
        return area
    
def main():
    # Create three RegularPolygon objects
    rp1 = RegularPolygon()
    rp2 = RegularPolygon(6, 4)
    rp3 = RegularPolygon(10, 4, 5.6, 7.8)
    
    # Display Perimeter and area of each RegularPolygon object
    print("Perimeter of Object1:", rp1.getPerimeter())
    print("Area of Object1:", format(rp1.getArea(), ".2f"))
    print()
    print("Perimeter of Object2:", rp2.getPerimeter())
    print("Area of Object2:", format(rp2.getArea(), ".2f"))
    print()
    print("Perimeter of Object3:", rp3.getPerimeter())
    print("Area of Object3:", format(rp3.getArea(), ".2f"))
    

main() # Call the main function
        