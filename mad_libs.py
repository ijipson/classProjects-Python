#Izabel Jipson
#Mad Libs Program
#This program asks the user for random words and inputs them into a paragraph
#October 5, 2022

#This is a title to the Madlibs
print("Welcome to Fall MadLibs!")

#This section requests input from user for words or numbers

noun1= input ("\nGive me a noun. ")

number= input ("\nGive me a number. ")

month1= input ("\nGive me a month. ")

month2= input ("\nGive me another month. ")

noun2= input ("\nGive me another noun. ")

adjective= input ("\nGive me an adjective. ")

noun3= input ("\nGive me another noun. ")

plural_noun1= input ("\nGive me a plural noun. ")

plural_noun2= input ("\nGive me another plural noun. ")

verb_ed= input ("\nGive me a verb that ends in -ed. ")

plural_noun3= input ("\nGive me another plural noun. ")


#This section uses the input from the section above to print a paragraph using the given words

print ("\n\n    Fall, also known as " +noun1+ ", is one of the " +number+ " seasons of the year.")

print("\nIn the United States, fall takes place from "+month1.capitalize()+ " to " +month2.capitalize()+ ". Two holidays")

print( "\nthat happen during fall are " +noun2+ ", where people dress up in "+adjective+ " costumes")

print( "\nand \""+noun3.capitalize()+ " Day\", a time to give thanks. This is also harvest time, when " +plural_noun1)

print(" \nand " +plural_noun2+ " are "+verb_ed+" for us to eat fresh or bake into "+plural_noun3+ ".")
