#Izabel Jipson 
# Python program containing all three types of errors,
# syntax, runtime and logic
# This program should calculate a person's age in the year 2050.

# Ask for user's name (syntax error had different quotation mark"
name = input("\nWhat is your name?")
# Ask for the year the user was born (runtime error was input should have int() before it)
birthyear = int(input("\nWhat year were you born?"))
# calculate the user's age in 2050 (logic error should've been subtraction not addition)
yourAgeIn2050 = (2050 - birthyear)
# tell the user how old she will be
print("\nHey, " + name.capitalize() + " you will be " + str(yourAgeIn2050) + " in 2050")


