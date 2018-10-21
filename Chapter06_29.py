# 6.29 Write a program that prompts the user to enter a credit card number as an integer. 
# Display whether the number is valid or invalid.
# Sample Inputs [4388576018402626] , [4388576018410707]

# Return true if the card number is valid
def isValid(number):
    size = getSize(number) # Get number of digits in the number
    if size == 13 or size == 16: # Check is number of digits is 13 or 16
        if prefixMatched(number, 4) or prefixMatched(number, 5) or prefixMatched(number, 37) \
        or prefixMatched(number, 6): # Check if the number starts with 4, 5, 37 or 6
            if (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0:
                return "The credit card number is valid"
            else:
                return "The credit card number is invalid"
        else:
            return "The credit card number is invalid"
    else:
        return "The credit card number is invalid"   

# Return sum of doubled even place digits in number after adjustment if doubling results in two digits
def sumOfDoubleEvenPlace(number):
    size = getSize(number) # Get number of digits in the number
    sumOfDoubleEvenPlaceDigits = 0
    for i in range(1, size + 1):
        digit = number % 10
        number = number // 10
        if i % 2 == 0: # Check if even place digit
            digit = digit * 2 # double the digit
            sumOfDoubleEvenPlaceDigits += getDigit(digit) 
    return sumOfDoubleEvenPlaceDigits

# Return this number if it is a single digit, otherwise, return the sum of the two digits
def getDigit(number):
    sumOfDigits = 0
    if number % 10 == number: # Check if single digit
        return number
    else: # split digits and return their sum
        while number > 0:
            digit = number % 10
            number = number // 10
            sumOfDigits += digit
        return sumOfDigits 

# Return sum of odd place digits in number
def sumOfOddPlace(number):
    size = getSize(number) # Get number of digits in the number
    sumOfOddPlaceDigits = 0
    for i in range(1, size + 1):
        digit = number % 10
        number = number // 10
        if i % 2 != 0: # Check if odd place digit
            sumOfOddPlaceDigits += digit
    return sumOfOddPlaceDigits

# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    if getPrefix(number, 1) == d or getPrefix(number, 2) == d:
        return True
    else:
        return False

# Return the number of digits in d
def getSize(d):
    count = 0 # Count the number of digits
    while d > 0:
        d = d // 10
        count += 1
    return count

# Return the first k number of digits from number. If the number of digits in number is less than k, 
# return number
def getPrefix(number, k):
    size = getSize(number) # Get number of digits in the number
    if size < k:
        return number
    else:
        return number // 10 ** (size - k)
    
def main():
    number = eval(input("Enter a credit card number: ")) # Prompt the user to enter a credit card number
    print(isValid(number)) # Display result
    
main() # Call the main function
