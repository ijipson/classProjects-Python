#Izabel Jipson
#Taxes and Constants
#This program calculates PA and NJ taxes on a price
#14 December 2022

#This is where the initial price is entered
amount = float(input("Enter your total."))

#Constants for each state's tax percentage
PA_TAX=0.06
NJ_TAX=0.06625

#The calculation for final total plus tax
PA_Total= amount + (amount * PA_TAX)
NJ_Total = amount + (amount * NJ_TAX)

#Printing the final total to user
print ("\nYour total in Pennsylvania is $", PA_Total,".")
print ("\nYour total in New Jersey is $", NJ_Total,".")
