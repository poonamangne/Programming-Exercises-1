# 6.3 Write a test program that prompts the user to enter an integer 
# and reports whether the integer is a palindrome

# Return the reversal of an integer, e.g. reverse(456) returns 654
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
        return str(number) + " is a Palindrome" 
    else:
        return str(number) + " is not a Palindrome"
    
def main():
    number = eval(input("Enter an integer: ")) # Prompt the user to enter a number
    print(isPalindrome(number)) # Displays if the number is a palindrome
    
main() # Call the main function