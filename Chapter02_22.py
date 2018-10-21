# 2.22 Write a program to prompt the user to enter the number of years and 
# displays the population after that many years

# Prompt the user to enter the number of years
numberOfYears = eval(input("Enter the number of years: "))

# Constants
CURRENT_POPULATION = 312032486 
BIRTH_RATE = 7
DEATH_RATE = 13
NEW_IMMIGRANT_RATE = 45

# Compute total seconds in a year with 365 days
secondsPerYear = 365 * 24 * 60 * 60

# Compute births per year
birthsPerYear = secondsPerYear / BIRTH_RATE

# Compute deaths per year
deathsPerYear = secondsPerYear / DEATH_RATE

# Compute new immigrants per year
newImmigrantsPerYear = secondsPerYear / NEW_IMMIGRANT_RATE

# Compute change in population per year
annualPopulationChange = birthsPerYear - deathsPerYear + newImmigrantsPerYear

# Compute population and print the result
population = CURRENT_POPULATION + numberOfYears * annualPopulationChange
print("The population in", numberOfYears, "years is", round(population))