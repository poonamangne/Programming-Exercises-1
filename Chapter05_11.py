# 5.11 Write a program that prompts the user to enter the number of students 
# and each student’s score, and displays the highest and second highest scores.

# Prompt the user for number of students
numberOfStudents = eval(input("Enter number of students: "))

highestScore = 0 # Initialize highest score
secondHighestScore = 0 # Initialize second highest score

# Prompt the user for each student's score and compute the highest and second highest score
for n in range(numberOfStudents):
    score = eval(input("Enter student score: "))
    secondHighestScore = min(max(score, secondHighestScore), highestScore)
    highestScore = max(score, highestScore)

# Display result
print("Highest Score is", highestScore, "and Second highest score is", secondHighestScore)