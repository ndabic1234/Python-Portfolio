#Niki
#parity
#Create a program that prompts the user for a number and prints whether that number is even or odd.
#Functions\
def is_even(x):
    #How to use mod
    if x % 2==0:
        return True
    elif x % 2==1:
        return False
def parity():

#Collecting input
    num=int( input("Please enter a number: ") )
#Evaluate and print Even or Odd
    if is_even(num):
        print("Even")
    else:
        print("Odd")



#Main
parity()
