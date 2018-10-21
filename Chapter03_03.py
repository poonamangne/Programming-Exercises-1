# 3.3 Find the GPS locations for Atlanta, Georgia; Orlando, Florida; Savannah, Georgia; and 
# Charlotte, North Carolina from and compute the estimated area enclosed by these four cities

import math # Import math module

# Set the GPS locations - latitude and longitudes for the four cities
atlantaX, atlantaY = 33.7489954, -84.3879824
charlotteX, charlotteY = 35.2270869, -80.8431267
savannahX, savannahY = 32.0835407, -81.0998342
orlandoX, orlandoY = 28.5383355, -81.3792365

# Convert degrees into radians
atlantaX, atlantaY = math.radians(atlantaX), math.radians(atlantaY)
charlotteX, charlotteY = math.radians(charlotteX), math.radians(charlotteY)
savannahX, savannahY = math.radians(savannahX), math.radians(savannahY)
orlandoX, orlandoY = math.radians(orlandoX), math.radians(orlandoY)

# Constant
AVERAGE_EARTH_RADIUS = 6371.01

# Compute the distance between Atlanta and Charlotte
atlantaCharlotteDistance = AVERAGE_EARTH_RADIUS * math.acos(math.sin(atlantaX) * math.sin(charlotteX) 
                        + math.cos(atlantaX) * math.cos(charlotteX) * math.cos(atlantaY - charlotteY))

# Compute the distance between Atlanta and Savannah
atlantaSavannahDistance = AVERAGE_EARTH_RADIUS * math.acos(math.sin(atlantaX) * math.sin(savannahX) 
                        + math.cos(atlantaX) * math.cos(savannahX) * math.cos(atlantaY - savannahY))

# Compute the distance between Atlanta and Orlando
atlantaOrlandoDistance = AVERAGE_EARTH_RADIUS * math.acos(math.sin(atlantaX) * math.sin(orlandoX) 
                        + math.cos(atlantaX) * math.cos(orlandoX) * math.cos(atlantaY - orlandoY))

# Compute the distance between Savannah and Orlando
savannahOrlandoDistance = AVERAGE_EARTH_RADIUS * math.acos(math.sin(savannahX) * math.sin(orlandoX) 
                        + math.cos(savannahX) * math.cos(orlandoX) * math.cos(savannahY - orlandoY))

# Compute the distance between Savannah and Charlotte
savannahCharlotteDistance = AVERAGE_EARTH_RADIUS * math.acos(math.sin(savannahX) * math.sin(charlotteX) 
                        + math.cos(savannahX) * math.cos(charlotteX) * math.cos(savannahY - charlotteY))

# Compute the area of the triangle with cities Atlanta, Charlotte, Savannah
s1 = (atlantaCharlotteDistance + savannahCharlotteDistance + atlantaSavannahDistance) / 2
area1 = (s1 * (s1 - atlantaCharlotteDistance) * (s1 - savannahCharlotteDistance) 
         * (s1 - atlantaSavannahDistance)) ** 0.5

# Compute the area of a triangle with cities Atlanta, Orlando, Savannah
s2 = (atlantaOrlandoDistance + savannahOrlandoDistance + atlantaSavannahDistance) / 2
area2 = (s2 * (s2 - atlantaOrlandoDistance) * (s2 - savannahOrlandoDistance) 
         * (s2 - atlantaSavannahDistance)) ** 0.5

# Compute total area enclosed by the four cities and display the result
totalArea = area1 + area2
print("The estimated area enclosed is", round(totalArea, 2))
