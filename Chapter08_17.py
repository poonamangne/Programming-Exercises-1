# 8.17 Write a test program that prompts the user to enter two points, displays 
# the distance between them, and indicates whether they are near each other
# Sample Inputs [2.1, 2.3, 19.1, 19.2], [2.1, 2.3, 2.3, 4.2]

class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
    
    # Return the distance between two points of class Point
    def distance(self, p1):
        dist = ((self.__x - p1.__x) * (self.__x - p1.__x) + (self.__y - p1.__y) * (self.__y - p1.__y)) \
        ** 0.5
        return round(dist, 2)
        
    # Return a string representation
    def __str__(self):
        return str("(", self.__x, ",", self.__y, ")")
    
    # Return true if distance between the two points is less than 5
    def isNearBy(self, p1):
        if self.distance(p1) < 5:
            return True
        else:
            return False
    
    # Check if two points are near each other and displays message accordingly
    def checkDistance(self, p1):
        if self.isNearBy(p1):
            return "The two points are near each other"
        else:
            return "The two points are not near each other"
def main():
    # Prompt the user for two points
    x1, y1, x2, y2 = eval(input("Enter two points x1, y1, x2, y2: "))
    
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    
    print("The distance between the two points is", p2.distance(p1))
    print(p2.checkDistance(p1))
    
 
 
main() # Call the main function    
