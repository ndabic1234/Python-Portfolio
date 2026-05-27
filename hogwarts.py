#Niki
#hogwarts
#Create a program that prompts the user for their name and simulates being assigned one of the 4 hogwarts houses
#Int
import time
import random
#Functions
def main():
    while True:
        print("Welcome to Hogwarts!")
        name=input("What is your name?").lower()
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("....")
        time.sleep(1)
        print( house(name))
        decide=input("Would you like to be assigned to a different house?: ")
        if decide.lower()=="no":
            print("Goodbye!")
            break
        elif decide.lower()=="yes":
            print(f"You entered {decide}. Start over.")

#This function checks a name and returns a house
def house(name):
    if name=="harry" or name=="ron" or name=="hermione":
        return "Gryffindor"
    elif name=="newt" or name=="nymphadora" or name=="pomona":
        return "Hufflepuff"
    elif name=="luna" or name=="cho" or name=="filius":
        return "Ravenclaw"
    elif name=="voldemort" or name=="draco" or name=="severus":
        return "Slytherin"
    else:
        random_num=random.randint(1,4)
        if random_num==1:
            return "Gryffindor"
        elif random_num==2:
            return "Hufflepuff"
        elif random_num==3:
            return "Ravenclaw"
        elif random_num==4:
            return "Slytherin"
#Main
main()

