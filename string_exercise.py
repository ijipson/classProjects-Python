#Izabel Jipson
#String Exercises Program
#This program executes various strings and prints statements
#26 September 2022

#Part 1
#Quote  from   IBM   Chairman,   Thomas   Watson,   in   1943
quote = "I think there is a world market for maybe FIVE computers."


print("Original quote: " +quote)

print("\n Quote in Uppercase: "+quote.upper())

print("\n Quote in Lowercase: " +quote.lower())

print("\n As a Title: "+quote.title())

print ("\n Replacing FIVE with millions of: " +quote.replace("FIVE", "millions of"))

print("\n Using swapcase: "+quote.swapcase())

print("\n Original quote is still: "+quote)

#Part 2
#This section takes in user input
name=input("What is your name?")
print("Hello " +name.capitalize())

#This section uses input to print lines personalized to user
print("Happy Birthday to You")
print("Happy Birthday to You")
print("Happy Birthday Dear " +name.capitalize())
print("Happy Birthday to You!")

#This line allows user press ENTER to get the program to end
input("\n\nPress the enter key to exit,")

#Part 3
#A program to calculate the valie of some change in dollars

print("\nChange Counter Program")
print()
print("Please enter the count of each coin type.")

#This section takes in input of different coin amounts

#get number of quarters
quarters= input("Quarters= ")
quarters=int(quarters)

#get number of dimes
dimes = input("Dimes= ")
dimes=int(dimes)

#get number of nickels
nickels= input("Nickels= ")
nickels=int(nickels)

#get number of pennies
pennies= input("Pennies= ")
pennies= int(pennies)


#This section calculates the value of the change

print("\nYour total change= $",quarters*.25 + dimes*.10 + nickels*.05 + pennies*.01)



