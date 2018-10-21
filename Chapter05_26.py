# 5.26 Write a program to sum the series of odd number fractions

# Initialize the start number, end number, sum of the series
startNum = 1
endNum = 99
sumOfSeries = 0

# Compute sum of the series
for nextNum in range(startNum, endNum, 2):
    sumOfSeries = sumOfSeries + nextNum / (nextNum + 2)

# Display result
print(format(sumOfSeries, ".4f"))
