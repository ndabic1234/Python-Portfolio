#Niki
#weather
#Create a program that advises you on what clothing to wear and accessories to bring based on temperature given
#Functions
def attire():
    temp=input("What is the temperature today?")
    if int(temp) >= 90:
        print("Wear a short sleeve shirt, pair of shorts, and sunglasses")
    elif int(temp) >= 70:
        print("Wear a short sleeve shirt and pair of shorts")
    elif int(temp) >= 40:
        print("Wear a large jacket, pair of pants, a hat and gloves")
    else:
        print("Wear a winter coat, pair of thick pants, a hat, and gloves")

#Main
attire()
