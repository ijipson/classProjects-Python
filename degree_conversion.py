#Izabel Jipson
#Conversion Program
#Convert degrees from fahrenheit to celcius
#17 October 2022

#This section asks user to specify which unit degrees they are giving

while True:
    dt= input("\nIs your degree in Fahrenheit or Celcius? Respond with F or C ")
    if dt.capitalize() in ("F, C"):
        print ("\n   You chose " +dt.capitalize())
        break
    else:
        print ("\n   I do not understand that letter please respond with F or C")
        continue
    

#This section asks for the number of degrees to convert
dn= int(input("\n\nEnter degree "))
print ("\n   You chose " +str(dn)+ ".")


#This section converts the integer to F or C based on user input
if dt.capitalize()== "F":
    print ("\n\n"+str(dn)+" degrees Fahrenheit is equivalent to " , (dn-32)*(5/9), " degrees Celcius." )

    if dn > 90:
        print ("\nIt's way too hot!")

elif dt.capitalize()=="C":
    print ("\n\n"+str(dn)+" degrees Celcius is equivalent to " , dn*(9/5)+32, "degrees Fahrenheit." )

    if dn <= 0:
        print ("\nIt's way too cold!")
    
#Allows user to exit program
print (input("\n\nPress Enter to Exit."))

