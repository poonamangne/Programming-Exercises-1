# 10.9 Write a test program that prompts the user to enter a list of numbers and displays the mean 
# and standard deviation
# Sample Input [1.9 2.5 3.7 2 1 6 3 4 5 2]

# Create a list of integers
def createList():
    # Read numbers as a string from the console
    s = input("Enter numbers: ")
    items = s.split() # Extract items from the string
    myList = [eval(x) for x in items] # Convert items to numbers
    return myList # Return the list

# Compute the standard deviation of values
def deviation(x):
    m = mean(x) # Get mean
    result = 0
    for i in x:
        result += ((i - m) ** 2)
    deviation = (result / (len(x) - 1)) ** 0.5
    return deviation

# Compute the mean of a list of values
def mean(x):
    sum = 0
    for i in x:
        sum += i
    mean = sum / len(x)
    return mean

def main():
    # Create a list of n numbers
    myList = createList()
   
    # Display the mean of the numbers in the list
    print("The mean is " + format(mean(myList), ".2f"))
    
    # Display the standard deviation of the numbers in the list
    print("The standard deviation is " + format(deviation(myList), ".5f"))
 


main() # Call the main function  
    