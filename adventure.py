#Niki
#adventure
#Create a program that takes the user on a mini text adventure. Each choice leads to a new situation using nested if statements.
#Functions
def adventure():
    print("Welcome to the Jungle Book!")
    weapon=input("Would you prefer a sword or bow and arrow as your weapon to protect you?: ")
    if weapon=="sword":
        print("Amazing! You have started to craft your sword!")
        sword_enhance=input("Would you prefer your sword made out of diamond or gold?: ")
        if sword_enhance=="diamond":
            print("Great choice! Your sword now has great durability!")
        elif sword_enhance=="gold":
            print("Who doesn't love gold on everything? Great choice!")
    elif weapon=="bow and arrow":
        print("Amazing! You have started to craft your bow and arrow!")
        bow_enhance=input("Would you prefer poisonous or fiery tips on your arrows?: ")
        if bow_enhance=="poisonous":
            print("Deadly and effective choice!")
        elif bow_enhance=="fiery":
            print("No danger would dare to get close to you now!")
#Main
adventure()
