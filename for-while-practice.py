#Izabel Jipson

#Program 1
a= int(input("Enter a positive number. "))
if (a<=0):
    print ("Input is illegal, program is terminated")
else:
    num=0
    while (a>=num):
        print (a, end=" ")
        a=a-1
print ()

#Program 2
import random

heads=0
tails=0

for i in range(1000000):
    num=random.randint(0,1)
    
    if num==0:
        heads+=1
    else:
        tails+=1

print ("Heads:",heads,"Tails:", tails)

#Program 3
import random 	
word= input("Enter a phrase.")

for i in range (3):
    position = random.randint(0,len(word)-1)
    print (word[position],end="")
