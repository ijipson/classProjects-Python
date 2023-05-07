#Izabel Jipson
#Strings and Indexing Program
#This program will answer various prompts about the word supercalifragilisticexpialidocious

word=("supercalifragilisticexpialidocious")
print (word)

#tells me the length of the word
print ("\nThe length of this word is:",len(word), "letters.")

#tells me if the letter “z” is in the word
if ("z" in word):
    print ("\nThe letter z is in this word.")
else:
    print("\nThe letter z is not in this word.")
    
#prints three random letters from the word (use indexing or slicing)
import random 					
position = random.randint(0,len(word))
position2 = random.randint(0,len(word))
position3 = random.randint(0,len(word))
print ("\nThree random letters from this word:",word[position],word[position2],word[position3])
