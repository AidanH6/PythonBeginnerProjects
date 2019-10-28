"""
Create a rock-paper-scissors game.
Ask the player to pick rock, paper or scissors.
Have the computer chose its move.
Compare the choices and decide who wins.
"""

import random

playing = True
score = { "Computer" : 0 , "Human" : 0 }
moves = [ 'Rock', 'Paper', 'Scissors' ]

def show_scores(score) :
    return "Human: {Human} - Computer: {Computer}".format(Human=score["Human"], Computer=score["Computer"])

while playing:
    roll = str(input( "Select a move: Rock, Paper or Scissors! Press Q to stop: ").capitalize())
    rnd = random.randint(0,2)
    Cmove = moves[rnd]
     
    if roll == "Q":
        exit()
    elif roll not in moves:
        print("I could't understand that move?")
    else:
        if roll == Cmove:
            print("Draw! You chose {roll} and the computer chose {Cmove}! No points this time".format(roll=roll, Cmove=Cmove))
        # Rock
        elif roll == "Rock" and Cmove == "Paper":
            print("Paper beats rock, computer wins!")
            score["Computer"] += 1
        elif roll == "Rock" and Cmove == "Scissors":
            print("Rock beats Scissors, you win!")
            score["Human"] += 1
        # Paper
        elif roll == "Paper" and Cmove == "rock":
            print("Rock beats Paper, computer wins!")
            score["Computer"] += 1
        elif roll == "Paper" and Cmove == "Scissors":
            print("Scissors beats Paper, you win!")
            score["Human"] += 1
        # Scissors
        elif roll == "Scissors" and Cmove == "Rock":
            print("Rock beat scissors, computer wins!")
            score["Computer"] += 1
        elif roll == "Scissors" and Cmove == "Paper":
            print("Scissors beats paper, you win!")
            score["Human"] += 1
            
        print( show_scores(score) )