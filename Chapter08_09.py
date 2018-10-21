# 8.9 Write a test program that prompts the user to enter a binary number 
# and displays the corresponding hexadecimal value.
# Sample Input [1100111100111101]

# Parse a binary number into a hex number
def binaryToHex(binaryValue):  
    hexValue = ""
    s1 = binaryValue
    while s1 != "":
        value = 0 # Value for last 4 characters from right
        if len(s1) > 4:
            s2 = s1[0: len(s1) - 4] # Remainder characters 
            s1 = s1[len(s1) - 4:len(s1)] # Last 4 characters
        for i in range(0, len(s1)): # Calculate decimal equivalent for last 4 characters
            value += int(s1[len(s1) - i - 1]) * (2 ** i) 
        if 0 <= value <= 9:
            hexValue = chr(value + ord('0')) + hexValue # Calculate hexadecimal and concatenate
        else: 
            hexValue = chr(value - 10 + ord('A')) + hexValue # Calculate hexadecimal and concatenate
        s1 = s2
        s2 = "" # Reset 
    return hexValue

def main():
    # Prompt the user for input
    binaryValue = input("Enter a binary number: ")

    # Display binary in hexadecimal format
    print("Hexadecimal: ", binaryToHex(binaryValue))
 
 
 
main() # Call the main function