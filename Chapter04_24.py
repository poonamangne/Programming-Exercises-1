# 4.24 Write a program that simulates picking a card from a deck of 52 cards.

import random # Import random module

# Generate a random rank
rankNumber = random.randint(1, 13)

# Compute rank from rank number
if rankNumber == 1:
    rank = "Ace"
elif rankNumber == 2:
    rank = "2"
elif rankNumber == 3:
    rank = "3"
elif rankNumber == 4:
    rank = "4"
elif rankNumber == 5:
    rank = "5"
elif rankNumber == 6:
    rank = "6"
elif rankNumber == 7:
    rank = "7"
elif rankNumber == 8:
    rank = "8"
elif rankNumber == 9:
    rank = "9"
elif rankNumber == 10:
    rank = "10"
elif rankNumber == 11:
    rank = "Jack"
elif rankNumber == 12:
    rank = "Queen"
else:
    rank = "King"

# Generate a random suit
suitNumber = random.randint(1, 4)

# Compute suit from suit number
if suitNumber == 1:
    suit = "Clubs"
elif suitNumber == 2:
    suit = "Diamonds"
elif suitNumber == 3:
    suit = "Hearts"
else:
    suit = "Spades"
    
# Display the result
print("The card you picked is the", rank, "of", suit)