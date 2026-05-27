#Niki
#Calculator
#Create a program that prompts users to enter two numbers, an operator, and prints the result of the operation
#Functions
def main():
#Welcome message
    print("Welcome to Simple Calculator!")
    print("----------------------------")
#Collect input
    num1=int( input("Please enter a number: "))
    num2=int( input("Please enter a number: "))
    operator=input("Please enter an operator(+,-,*,/): ")
#Perform Operation
    if operator=="+":
        print(calc_sum(num1,num2))
    elif operator=="-":
        print(calc_sub(num1,num2))
    elif operator=="/":
         print(calc_div(num1,num2))
    elif operator=="*":
         print(calc_mult(num1,num2))
#This function adds two numbers and returns the total
def calc_sum(x,y):
    return x+y
def calc_sub(x,y):
    return x-y
def calc_div(x,y):
    return x/y
def calc_mult(x,y):
    return x*y
#Main
main()
