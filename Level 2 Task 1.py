'''LEVEL 2 TASK 1
GUESSING GAME'''

import random

def guessgame():
    computer=random.randint(1,100)
    guess=False
    while guess==False:
        try:
            user=int(input("Enter your Guess:"))
        except:
            print("Please Enter Integer Value")
            user=int(input("Enter your Guess:"))
        if user>computer:
            if user>1.5*computer:
                print("Too High!")
            else:
                print("High!")
            print("Try Again!")
        elif user<computer:
            if 1.5*user<computer:
                print("Too low!")
            else:
                print("Low!")
            print("Try Again!")
        else:
            print("\nWOW!\nYou Guessed right!")
            guess=True

print("***GUESSING GAME (1-100)***\n")
play=0
while play==0:
    guessgame()
    try:
        play=int(input("\nEnter 0 for another game:"))
    except ValueError:
        break
    
