# 6.24 Write a program that displays the first 100 palindromic prime numbers


# Check whether number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False  # number is not a prime
        divisor += 1
    return True  # number is prime


# Return the reversal of an integer
def reverse(number):
    reverseNumber = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        reverseNumber = reverseNumber * 10 + digit
    return reverseNumber


# Check if number is a palindrome
def isPalindrome(number):
    reverseNumber = reverse(number)
    if number == reverseNumber:
        return True  # number is a palindrome
    else:
        return False  # number is not a palindrome


# Print first n palindromic primes
def printPalindromicPrimeNumbers(numberOfPalindromicPrimes):
    NUMBER_OF_PALINDROME_PRIMES_PER_LINE = 10  # Display 10 per line
    count = 0  # Count the number of palindromic prime numbers
    number = 2  # A number to be tested for palindromic primeness
    # Repeatedly find palindromic prime numbers
    while count < numberOfPalindromicPrimes:
        # Check if palindromic prime and increment the count
        if isPrime(number) and isPalindrome(number):
            print(format(number, ">5d"), end = " ")
            count += 1
            if count % NUMBER_OF_PALINDROME_PRIMES_PER_LINE == 0:
                print()  # Move to new line
        number += 1


def main():
    numberOfPalindromicPrimes = 100  # Set number of palindromic primes
    printPalindromicPrimeNumbers(numberOfPalindromicPrimes)


main()  # Call the main function
