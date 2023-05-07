#Izabel Jipson
#Final Project - Bank ATM
#This program functions similarly to an ATM
#January 5 2023

#functions
def display_menu():
    print ("Banking Menu:")
    print("\nWelcome to the Bank of Izabel!")
    print("\n     1) Check Balance")
    print("     2) Make a deposit")
    print("     3) Request a withdrawal")
    print("     0) Exit the program")
    

def deposit():
    add=float(input("Enter the amount you want to deposit. "))
    return add
        
#main program

display_menu()
choice=int(input("\nEnter your choice > "))
if choice==1:
    import random
    balance = random.randint(100,5000)
    print ("Your current balance is $",balance)
    
elif choice==2:
    print (deposit())
    

elif choice==3:
    withdrawal()
elif choice==0:
    exit
else:
    print ("Your choice is invalid please try again.")
    display_menu()

