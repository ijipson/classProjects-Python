#Izabel Jipson
#19 September 2022
#Responding Form
#This program requests user input and outputs responses using that information


#This input asks for name and responds with a compliment
name = input("What is your name?")
print(name+" is such a pretty name!")

#This input asks for a color and responds
color= input("\nWhat is your least favorite color?")
print("I agree " +color+ " is not the best color.")

#This input asks for a drink and responds based on the response
drink=input("\nWhat drink do you order on airplanes?")
sprite= True
if drink.lower()=="sprite":
    print("I order sprite too!")
else:
    print("I usually order sprite but " +drink+ " is good too!")

#This input asks for the user's age and responds based on the number
age=int(input("\nHow old are you?"))
if age>16:
    print("Wow " +str(age)+ "? you are old!")
if age==16:
    print("Hey " +str(age)+ "? me too!")
if age<16:
    print("Aww " +str(age)+ "? you are basically a baby.")


#Salutation string to end the conversation form
print("\n\nIt was nice talking to you have a good day!")

#This string prompts the user to hit enter to exit
input ("Press the enter key to exit.")
