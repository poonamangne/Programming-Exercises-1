# 6.2 Write a function that computes the sum of the digits in an integer

# Compute sum of the digits
def sumDigits(n):
    sumOfDigits = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        sumOfDigits += digit
    return sumOfDigits

def main():
    number = eval(input("Enter an integer: ")) # Prompt the user to enter a number
    print("Sum of the digits is", sumDigits(number)) # Display sum of the digits
    
main() # Call the main function