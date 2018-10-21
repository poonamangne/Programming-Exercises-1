# 8.3 Write a program that prompts the user to enter a password and displays valid password 
# if the rules are followed or invalid password otherwise.
# Sample Inputs [43GRfdf], [dR#t3dT#], [dRt3dT210], [dkTw3dsP]

# Check if password is valid
def checkPassword(p):
    if isLengthValid(p) and isCharValid(p) and isNumberOfDigitsValid(p):
        return "Valid Password"
    else:
        return "Invalid Password"

# Check length of password criteria
def isLengthValid(p):
    if len(p) >= 8:
        return True
    else:
        return False
    
# Check number of digits password criteria
def isNumberOfDigitsValid(p):
    length = len(p)
    count = 0 # Count number of digits
    for i in range(0, length):
        if 48 <= ord(p[i]) <= 57:
            count += 1
    if count >= 2:
        return True
    else:
        return False

# Check digits and alphabets password criteria    
def isCharValid(p):
    length = len(p)
    for i in range(0, length):
        if (48 <= ord(p[i]) <= 57) or (65 <= ord(p[i]) <= 90) or (97 <= ord(p[i]) <= 122):
            if i == length - 1:
                return True
            else:
                continue      
        else:
            return False       
    
def main():
    # Prompt the user for inputs
    password = input("Enter a password: ")
    
    # Display result
    print(checkPassword(password))
 
 
 
main() # Call the main function

