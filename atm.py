#Init
#Niki
#atm
#This program defines a function 3 functions that simulate transactions in an atm
#Functions
money=1000000
print(f"You're current balance is {money}")
def deposit():
    global money
    deposit=input("How much money would you like to deposit into your account?: ")
    money=money+int(deposit)
def withdraw():
    global money
    withdraw=input("How much money would you like to withdraw from your account: ")
    money=money-int(withdraw)
def total():
    global money
    print(f"New amount: {money}")
#Main
deposit()
withdraw()
total()
