import random
import time

replies = [ "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely",
            "You may rely on it.",
            "As I see it yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "All signs point to yes.",
            "Reply hazy - try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful." ]

def eight_ball():
    question = str(input("What do you wish to know? \n").lower())
    print("The question was: " + question)
    time.sleep( 1 )
    print("Hmmmmmm")
    time.sleep( 2 )
    print(replies[random.randint(1,21)])
    play_loop()

def play_loop():
    again = str(input("Would you like to play again?(y/n) \n").lower())
    if again == 'y':
        eight_ball()
    elif again == 'n':
        print( "Play again soon!")
    else:
        print("I didn't quite get that?")
        play_loop()


eight_ball()
    
