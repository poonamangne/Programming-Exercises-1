# 5.35 Write a program to find four perfect numbers less than 10,000.

# Compute the perfect numbers less than 10000 and display result
print("The four perfect integers less than 10000 are: ", end = "")
for i in range(1, 10000):
    sumOfDivisors = 0
    n = i // 2
    for j in range(1, n + 1):
        if i % j == 0:
            sumOfDivisors = sumOfDivisors + j;
    if sumOfDivisors == i:
        print(i, end = " ")
