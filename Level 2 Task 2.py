'''LEVEL 2 TASK 2
NUMBER GUESSER'''

import random

def guessgame(ll,ul):
    computer=random.randint(ll,ul)
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

print("***NUMBER GUESSER***\n")
play=0
while play==0:
    try:
        ll=int(input("Enter lower limit:"))
        ul=int(input("Enter upper limit:"))
        guessgame(ll,ul)
    except ValueError:
        print("\n*ERROR*\n Enter Integer Limit")
        ll=int(input("Enter lower limit:"))
        ul=int(input("Enter upper limit:"))
        guessgame(ll,ul)
    try:
        play=int(input("\nEnter 0 for another game:"))
    except:
        break       


    
