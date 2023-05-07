#Izabel Jipson
#22 September 2022
#Calculator Program
#This program asks user for input and calculates equations using that input


#This section asks the user to input name and two numbers
name = input("What is your name?")

a= int(input('\n' "Pick a number from 1-10."))
b= int(input("Pick another number from 1-10."))


#This section prints the users name and math problems and answers
print('\n' "Hi "+name+ "! Here is math with your two numbers...")

print ('\n', a,"+",b, "=",a+b,"     ", a,"-",b, "=",a-b,"      ",a,"*",b, "=",a*b)

print('\n',a,"//",b,"=",a//b,"     ",a,"/",b,"=",a/b,"     ",a,"%",b,"=",a%b )


#This section prompts the user to exit the program
print (input('\n'"Press the enter key to exit"))



