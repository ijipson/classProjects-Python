#Izabel Jipson
#While Loops Practice
#This is a practice program for loops

#Print the squares of the first 25 odd, positive integers.
num=1
cnt=0
while (cnt<=25):
    num=num+2
    cnt= cnt+1
    print (num*num)


#Ask the user for a number and store it in a variable called xValue.  Repeatedly print the value of the xValue, decreasing it by 0.5 each time, as long as xValue remains positive.
xValue= int(input("Enter a number "))
while (xValue>=0):
    print (xValue)
    xValue=xValue-0.5
    
#Print all even numbers between 1 to 100.
num=0
while (num<=100):
    print(num)
    num=num+2

#Get numbers from the user and add them together.  You should get 5 numbers and print the sum of the 5 numbers at the end.  You MUST use a loop to get one number at a time!

cnt=1
total=0
while (cnt<=5):
    cnt=cnt+1
    num= int(input("Enter a number"))
    total=total+num
    print (total)
    
