# 6.5 Write a test program that prompts the user to enter three numbers 
# and invokes the function to display them in increasing order

# Sorts the numbers in increasing order and displays result
def displaySortedNumbers(num1, num2, num3):
    for i in range(1, 3):     
        if num1 > num2:
            num1, num2 = num2, num1 # swap num1 and num2
        if num2 > num3:
            num2, num3 = num3, num2 # swap num2 and num3
    print("The sorted numbers are", num1, num2, num3)
    
def main():
    number1, number2, number3 = eval(input("Enter three numbers: ")) # Prompt the user for input
    displaySortedNumbers(number1, number2, number3)
    
main() # Call the main function

