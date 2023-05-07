#Izabel Jipson
#Magic 8 Ball Programming
#This program asks a user to input a question and gives a random response back

#Section explaining program
print ("Welcome to the Magic 8 Ball!")
print ("\nThe 8 Ball will ask you for a question and give you an answer based on its omniscient knowledge.")

#Asks user to input question but does not do anything with question
input("\nWhat is your question? ")


#This line imports random library
import random

    
#This section assigns different phrases to each number in the range and randomly prints one
num=random.randrange(1,8)
if  num==1:
    print("\nSigns Point to Yes")
elif num==2:
    print("\nMaybe")
elif num==3:
    print("\nNo")
elif num==4:
    print("\nReply Hazy, Try Again Later")
elif num==5:
    print("\nDon't Count On It")
elif num==6:
    print("\nBetter Not Tell You Now")
elif num==7:
    print("\nOutlook Good")
elif num==8:
    print("\nVery Doubtful")
else:
    print("\nConcentrate and Ask Again")


#This section allows the user to exit the program
input ("\n\nPress Enter to Exit Program")
