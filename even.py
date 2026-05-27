#Niki
#even
#Create a program that takes in a number and prints all even numbers from 2 up to that number. This reinforces loops and counting patterns.
#Functions
def even():
    number=int(input("Please type in a number: "))
    if number % 2==0:
            for i in range(2,number,2):
                print(i)
    print(number)
#Main
even()
