#Izabel Jipson
#Lists Practice
#This program builds a shopping list
#December 21, 2022

#initial greeting and explanation of program
print("Welcome to your shopping list, enter items one by one into the program and once you are done type exit to complete and print your list.")

#Create an empty Python list.
shopping=[]

#Ask the user for an item.
item="enter"
while item!="exit":
    item=input ("\nEnter an item. ")

#If the item IS NOT already in the list (make the program check for it), it should be added and a message printed saying it was successfully added.
    if item not in shopping:
        shopping.append(item)
        print ("\nSuccessfully added ",item, "to list.")
        item=input("To add a different item hit enter, to exit and print type exit here.")

#If the value IS in the list, it should not be added, and a message is printed saying it was not added because it is already in the list.
    else:
        print ("Entered item is already in list. ")

#Prints total list of items 
print ("\nList: ")
for item in shopping:
        print (item)
