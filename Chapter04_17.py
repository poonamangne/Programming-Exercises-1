# 4.17 Write a program that plays the popular scissor-rock-paper game

import random # Import random module

# Prompt the user for input
user = eval(input("Enter scissor (0), rock (1), paper (2): "))

# Compute user choice
if user == 0:
    userChoice = "scissor"
elif user == 1:
    userChoice = "rock"
elif user == 2:
    userChoice = "paper"
else: 
    userChoice = "error"
    
# Proceed if valid user choice
if userChoice != "error":
    
    # Generate a random choice for computer
    computer = random.randint(0, 2)
            
    # Compute computer choice   
    if computer == 0:
        computerChoice = "scissor"
    elif computer == 1:
        computerChoice = "rock"
    elif computer == 2:
        computerChoice = "paper"  

    # Check check choices and display result
    if userChoice == computerChoice:
        print("The computer is " + computerChoice + ". You are " + userChoice + " too. It is a draw.")
    elif userChoice == "scissor":
        if computerChoice == "rock":
            print("The computer is " + computerChoice + ". You are " + userChoice + ". Computer won.")
        else:
            print("The computer is " + computerChoice + ". You are " + userChoice + ". You won.")
    elif userChoice == "rock":
        if computerChoice == "paper":
            print("The computer is " + computerChoice + ". You are " + userChoice + ". Computer won.")
        else:
            print("The computer is " + computerChoice + ". You are " + userChoice + ". You won.")
    else:
        if computerChoice == "scissor":
            print("The computer is " + computerChoice + ". You are " + userChoice + ". Computer won.")
        else:
            print("The computer is " + computerChoice + ". You are " + userChoice + ". You won.")
else:
    print("Incorrect choice!")