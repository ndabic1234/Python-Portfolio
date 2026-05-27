#Niki
#coffee
#Create a program that asks the user a few questions about preferences (sweet, hot/cold, caffeine, etc.) and “recommend” a drink
#Functions
def drink():
    print("Welcome to Python Cafe!")
    #Hot Recommendation
    temp=input("Do you want a cold or hot drink?: ")
    if temp=="hot":
        taste=input("Do you want a sweet drink (yes,no)?: ")
        if taste=="yes":
            print("We recommend a Hot Chocolate!")
        elif taste=="no":
            print("We recommend a Black Coffee!")
    #Cold Recommendation
    elif temp=="cold":
        taste=input("Do you want a sweet drink (yes,no)?: ")
        if taste=="yes":
            print("We recommend an Iced Latte!")
        elif taste=="no":
            print("We recommend a Cold Brew!")
#Main
drink()

