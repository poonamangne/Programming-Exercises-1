# 6.10 Write a program to find the number of prime numbers less than 10,000

# Check whether number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False # number is not a prime
        divisor += 1
    return True # number is prime

# Count number of prime numbers less than n
def numberOfPrimes(n):
    count = 0 # Count the number of prime numbers
    for i in range(2, n):
        # Check if prime and increment the count
        if isPrime(i):
            count += 1
    return count
            
def main():
    n = 10000
    print("There are", numberOfPrimes(n), "prime numbers less than", n)
    
main() # Call the main function