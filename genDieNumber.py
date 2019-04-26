import sys
import random

# generate list of dice numbers & record dice type
# @return tuple (number list, type list)
def genDieNumber(n):
    diceNum_list = []
    diceType_list = []
    diceType = ""
    start = random.randint(0,1)
    if start == 0:
        diceType = "F"
    elif start == 1:
        diceType = "L"
    for i in range(0,n):
        diceType_list.append(diceType)
        if diceType == "F":
            diceNum_list.append(fairDice())
            nextDice = random.uniform(0,1)
            if nextDice <= 0.8:
                diceType = "F"
            else:
                diceType = "L"
        elif diceType == "L":
            diceNum_list.append(loadDice())
            nextDice = random.uniform(0,1)
            if nextDice <= 0.7:
                diceType = "L"
            else:
                diceType = "F"
    return (diceNum_list,diceType_list)

# throw a fair dice
# @return int number on dice
def fairDice():
    return random.randint(1,6)

# throw a loaded dice
# @return int number on dice
def loadDice():
    dice = [1,2,3,4,5,6,6,6,6,6]
    return random.choice(dice)