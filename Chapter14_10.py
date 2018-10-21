# 14.10 Write a program that repeatedly prompts the user to enter a capital for a state using a
# dictionary to store the pairs of states and capitals so that the questions are randomly displayed

import random


def main():
    statesCapitals = {"Alabama":"Montgomery", "Alaska":"Juneau", "Arizona":"Phoenix",
                      "Arkansas":"Little Rock", "California":"Sacramento", "Colorado":"Denver",
                      "Connecticut":"Hartford", "Delaware":"Dover", "Florida":"Tallahassee",
                      "Georgia":"Atlanta", "Hawaii":"Honolulu", "Idaho":"Boise", "Illinois":"Springfield",
                      "Indiana":"Indianapolis", "Iowa":"Des Moines", "Kansas":"Topeka", "Kentucky":"Frankfort",
                      "Louisiana":"Baton Rouge", "Maine":"Augusta", "Maryland":"Annapolis", "Massachusetts":"Boston",
                      "Michigan":"Lansing", "Minnesota":"St. Paul", "Mississippi":"Jackson", "Missouri":"Jefferson City",
                      "Montana":"Helena", "Nebraska":"Lincoln", "Nevada":"Carson City", "New Hampshire":"Concord",
                      "New Jersey":"Trenton", "New Mexico":"Santa Fe", "New York":"Albany", "North Carolina":"Raleigh",
                      "North Dakota":"Bismarck", "Ohio":"Columbus", "Oklahoma":"Oklahoma City", "Oregon":"Salem",
                      "Pennsylvania":"Harrisburg", "Rhode Island":"Providence", "South Carolina":"Columbia",
                      "South Dakota":"Pierre", "Tennessee":"Nashville", "Texas":"Austin", "Utah":"Salt Lake City",
                      "Vermont":"Montpelier", "Virginia":"Richmond", "Washington":"Olympia", "West Virginia":"Charleston",
                      "Wisconsin":"Madison", "Wyoming":"Cheyenne"}

    correctCount = 0
    stateList = list(statesCapitals.keys())

    for i in range(0, len(stateList)):
        key = random.choice(stateList)
        userAnswer = input("Capital of " + str(key) + "?")
        if userAnswer.lower() == str(statesCapitals[key]).lower():
            print("Correct!")
            correctCount += 1
        else:
            print("Incorrect!")
        stateList.remove(key)

    print("Total correct count is", correctCount)


main()
