# 8.6 Write a test program that prompts the user to enter a string and displays the 
# number of letters in the string.
# Sample Inputs [ssdegd], [de324fdsf], [sd$@3ferR]

# Count the number of letters in a string
def countLetters(s):
    count = 0 # Count number of letters
    length = len(s)
    for i in range(0, length):
        if (65 <= ord(s[i]) <= 90) or (97 <= ord(s[i]) <= 122):
            count += 1
    return count

def main():
    # Prompt the user for input
    s = input("Enter a string: ")
    
    # Display result
    print("Number of letters in the string:", countLetters(s))
 
 
 
main() # Call the main function