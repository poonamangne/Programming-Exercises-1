# 5.36 Revise the Rock Scissor Paper program to let the user play continuously until either the user 
# or the computer wins more than two times.

import random # Import random module

# Initialize the number of user and computer wins
userWins = 0
computerWins = 0

# Check condition and proceed
while userWins <= 2 and computerWins <= 2:
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
        print("Incorrect choice!") # Report incorrect choice
        continue
    
    # Generate a random choice for computer
    computer = random.randint(0, 2)
    
    # Compute computer choice   
    if computer == 0:
        computerChoice = "scissor"
    elif computer == 1:
        computerChoice = "rock"
    elif computer == 2:
        computerChoice = "paper"  
    
    # Check the choices and display result
    if userChoice == computerChoice:
        print("The computer is " + computerChoice + ". You are " + userChoice + " too. It is a draw.")
    elif userChoice == "scissor":
        if computerChoice == "rock":
            print("The computer is " + computerChoice + ". You are " + userChoice + ". Computer won.")
            computerWins += 1
        else:
            print("The computer is " + computerChoice + ". You are " + userChoice + ". You won.")
            userWins += 1
    elif userChoice == "rock":
        if computerChoice == "paper":
            print("The computer is " + computerChoice + ". You are " + userChoice + ". Computer won.")
            computerWins += 1
        else:
            print("The computer is " + computerChoice + ". You are " + userChoice + ". You won.")
            userWins += 1
    else:
        if computerChoice == "scissor":
            print("The computer is " + computerChoice + ". You are " + userChoice + ". Computer won.")
            computerWins += 1
        else:
            print("The computer is " + computerChoice + ". You are " + userChoice + ". You won.")
            userWins += 1
            
print("Computer Score:", computerWins,"User Score:", userWins)