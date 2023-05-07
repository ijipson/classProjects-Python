#Izabel Jipson
#1 December 2022
#Username and Password Program
#This program generates username and passwords


#Welcome the user and tell her what the program does.
print ("Welcome! This program will ask you for your first and last name one at a time and then give you a username and password")
import random
create="enter"

while (create!="exit"):
    
#Have her input a first name and last name.
    fname= input("\nEnter Your First Name ")
    lname= input ("\nEnter Your Last Name ")
    
#Generate the username like ijipson
    print ("\nUsername: ",(fname[0]+lname[0:7]).lower())

#Generate the password. Concatenate the first two characters of the last name with a random 3 digit number (must be three digits) and then with the first two characters of the first name.
#Output the new password (it must be all lowercase)
    num1= random.randint(0,9)
    num2= random.randint(0,9)
    num3= random.randint(0,9)
    print ("\nPassword: ", (lname[0:1] + str(num1) + str(num2) + str(num3) + fname[0:1]).lower())

#Let the person generate usernames and passwords for lots of different names (LOOP!)
    create=input("\nIf you would like to create another username and password type new otherwise type exit to leave the program. ")
    
else:
    print ("\nGoodbye!")
