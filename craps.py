#Izabel Jipson
#Craps Program
#This program randomly rolls two dice and returns output like craps game

import random
roll="enter"

#starts while loop for craps game
while (roll!="exit"):
    die1 = random.randint(1,6)
    die2 = random.randrange(6) + 1
    total = die1 + die2
    print ("\nYou rolled a", die1,"and a", die2, "for a total of", total)

#if statements to tell user whether they won
    if (total==7):
        print ("\nYou won")
    elif (total==11):
        print ("\nYou Won")

#elif statements to tell user they lost
    elif (total==2):
        print ("\nYou Lose")
    elif (total==3):
        print ("\nYou Lose")
    elif (total==12):
        print ("\nYou Lose")

#else statement to tell user to Roll Again 
    else:
        print ("\nRoll Again")
        
#Allows user to either replay using loop or exit project 
    roll= input ("\nTo replay hit enter. To stop playing type exit and hit enter")

