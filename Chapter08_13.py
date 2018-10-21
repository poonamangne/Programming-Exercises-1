# 8.13 Write a program that prompts the user to enter two strings and displays their common prefix
# Sample Inputs [distance, disinfection]

# Returns the longest common prefix of two strings s1 and s2
def prefix(s1, s2):
    i = 0
    j = 0
    commonPrefix = ""
    while j < len(s2) and i < len(s1):
        if s1[i] == s2[j]: # check if match then move to next character in both strings
            commonPrefix += s1[i]
            j += 1
            i += 1  
        else:
            break     
    return commonPrefix

def main():
    # Prompt the user for inputs
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")
    
    # Display result
    print("The longest common prefix of", s1, "and", s2, "is", prefix(s1, s2))
 
 
 
main() # Call the main function