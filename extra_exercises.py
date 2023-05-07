#Izabel Jipson
#Extra Exercises
#21 October 2022

#Exercise 1
print ("WELCOME TO THE ECHO CHAMBER")

#This line asks user for any string phrase
phrase= input("Type a phrase ")

#This line converts all characters to uppercase to mimic an echo
print(phrase.upper()+"!!!")




#Exercise 2
print ("\n\nSentence Generator")

#This section requests a user to input various words
noun= input("\n  Please enter a noun ")
verb= input("\n  Please enter a verb ")
adjective= input("\n  Please enter a adjective ")
adverb= input("\n  Please enter a adverb ")

#This line uses those words to create a sentence
print ("\nThe " +adjective+" "+noun+" "+adverb+" " +verb+ ".")





#Exercise 3
print ("\n\nAverage Calculator")

#This section requests 5 integers from the user
n1= int(input("\n  Please enter your first number "))
n2= int(input("\n  Please enter your second number "))
n3= int(input("\n  Please enter your third number "))
n4= int(input("\n  Please enter your fourth number "))
n5= int(input("\n  Please enter your fifth number "))

#This line finds and prints the mean of those numbers
print ("\nThe average of your 5 integers is ", (n1+n2+n3+n4+n5)/5)




#Exercise 4
print ("\n\nCircle Math")

#This line requests the radius of the circle from the user
r= int(input("\n  Please enter the radius of your circle "))

#This line imports math and calculates circumference and area
import math
print ("\n\nThe circumference of your circle is ", 2*r*math.pi)
print ("\nThe area of your circle is ",math.pi*r**2)





#Exercise 5
print ("\n\nAge Status")
age=int(input("\nHow old are you? "))

#This section takes the age input and prints different responses based on the age
if 18<=age<65:
    print("\nYou are an adult.")
elif age<18:
    print("\nYou are a minor.")
elif age>=65:
    print("\nYou are a senior citizen")





#Exercise 6
print ("\n\nAre You a Genius?")
name= input("\n  What is your name? ")

#This section generates a random number and prints different responses based on that number *name has zero impact on outcome 
import random
x=random.randint (85,200)
if x>=160:
    print ("\nYou are a genius!")
elif x<160:
    print ("\nYou are average.")
