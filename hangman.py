"""
Create a program which selects a random name and then allows the user to try guess it
Like the real game, there should be blank spaces in the name
add a part of the body for every wrong letter
after too many wrong answers the game ends
"""

import random

RandomName = [ "aidan", "arthur", "oliver", "olivia", "mark", "mary", "winston", "moria", "romeo", "juliet", "desdamona", "othello" ]
wrongGuess = 0
tries = 0
Maxtries = 7
rndInt = random.randint(0,12)

guesses = []
name = RandomName[rndInt]
nLength = len(name)
printName = ['_'] * len(name)

def is_in_name(letter, name ):
    for i in range(0,nLength):
        if letter == name[i]:
            if printName[i] == '_':
                printName[i] = letter
                print( "Well done! You guessed a letter right. The guess now looks like {name}".format(name=printName))

while wrongGuess <= Maxtries:
    lGuess = str(input( "Enter a letter to try guess the word: ").lower())
    if wrongGuess == Maxtries:
        print("You have used up all your tries!")
        exit()
    if lGuess in name:
        is_in_name(lGuess, name)
    elif lGuess in guesses:
        guesses.append(lGuess)
        print( "{guess} has already been tried".format(guess=lGuess))
    elif lGuess not in name:
        wrongGuess += 1
        guesses.append(lGuess)
        print( "That letter is not in the name. You have had {tries} wrong tries!".format(tries=wrongGuess))
    if printName == name:
        print("Well done! You worked it out!")
        exit()
