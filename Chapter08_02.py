# 8.2 Write a program that prompts the user to enter two strings and then 
# checks whether the first string is a substring of the second string.

# Function to implement find
def find(s1, s2):
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]: # check if match then move to next character in both strings
            j += 1
            i += 1
        else:
            j += 1 # Move to next character in s2
            if(i != 0): # If only partial match, reset i and j to positions before partial match
                j -= i
                i = 0
    if i == 0 or i < len(s1): # If no match found return -1
        return -1
    else:
        return j - i # match found, return the position

# Checks if s1 is a substring of s2
def checkSubString(s1, s2):   
    if find(s1, s2) == -1:
        return "s1 is not a substring of s2"
    else:
        return "s1 is a substring of s2"
    

def main():
    # Prompt the user for inputs
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    
    # Display result
    print(checkSubString(s1, s2))
 
 
 
main() # Call the main function