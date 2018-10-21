# 1.11 Write a program to display the population for each of the next five years

# Constants
CURRENT_POPULATION = 312032486 
BIRTH_RATE = 7
DEATH_RATE = 13
NEW_IMMIGRANT_RATE = 45

# Compute total seconds in a year with 365 days
secondsPerYear = 365 * 24 * 60 * 60

# Compute births per year
birthsPerYear = secondsPerYear // BIRTH_RATE

# Compute deaths per year
deathsPerYear = secondsPerYear // DEATH_RATE

# Compute new immigrants per year
newImmigrantsPerYear = secondsPerYear // NEW_IMMIGRANT_RATE

# Compute change in population per year
annualPopulationChange = birthsPerYear - deathsPerYear + newImmigrantsPerYear

# Compute first year population and print the result
populationInYear1 = CURRENT_POPULATION + annualPopulationChange
print("1st Year Population:", populationInYear1)

# Compute second year population and print the result
populationInYear2 = populationInYear1 + annualPopulationChange
print("2nd Year Population:", populationInYear2)

# Compute third year population and print the result
populationInYear3 = populationInYear2 + annualPopulationChange
print("3rd Year Population:", populationInYear3)

# Compute fourth year population and print the result
populationInYear4 = populationInYear3 + annualPopulationChange
print("4th Year Population:", populationInYear4)

# Compute fifth year population and print the result
populationInYear5 = populationInYear4 + annualPopulationChange
print("5th Year Population:", populationInYear5)
