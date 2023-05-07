#Izabel Jipson
#Shopping Spree Program
#Keeps track of spending budget

#Gives intro to how to use program
print ("Enter the price of your items one at a time and when you finish entering all your items enter 0 to end the program and get your total.")

#Use a while loop to get the prices
total=0
price=1
while (price!=0):
    price= float(input("What is the price of your item "))
    total=total+price
    print ("You've spent $",total)

#Tells user their grand total
if (price==0):
    print ("Your total is ", total)

    
    


