"""
Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is.
After every guess, the computer should tell the user if the guess is higher or lower than the answer.
When the user guesses the correct number, print out a congratulatory message.
"""

import random

playing = True
tries = { "try": 0 }
compNum = random.randint(0,100)

while playing:
    guess = int(input("The computer has selected a number between 0 and 100. Try guess it!: "))
    if guess > 100:
        print("Invalid number. please enter it again.")
    if guess > compNum:
        print("That guess was higher than the computer's number!")
        tries['try'] += 1
    elif guess < compNum:
        print("That guess was lower than the computer's number!")
        tries['try'] += 1
    else:
        tries['try'] += 1
        print("You guessed right! It took you {tries} tries.".format(tries=tries['try']))
        exit()