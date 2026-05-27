#Niki
#Madlibs
#To create a fun and interactive game that allows users to input words and generate a nonsensical story.
#Init
import random
#Functions
def madlibs():
    bold1="\033[1m"
    bold2="\033[0m"
    yellow="\033[93m"
    place_list=["McDonalds", "Starbucks", "Burger King", "Panda Express"]
    name_list=["John", "Bob", "Greg", "Chuck"]
    adjective_list=["SPICY", "TASTY", "GROSS", "OILY"]
    verb_list=["ran", "jumped", "swam", "cried"]
    number_list=["1","2","3","4"]

#Place
    place=input("Please type in a place or the word 'random' if you can't decide: ")
    place=place.upper()
    if place=="RANDOM":
        place=random.choice(place_list)

#Name
    name=input("Please type in a name or the word 'random' if you can't decide: ")
    name=name.upper()
    if name=="RANDOM":
        name=random.choice(name_list)

#Adjective
    adjective=input("Please type in an adjective or the word 'random' if you can't decide: ")
    adjective=adjective.upper()
    if adjective=="RANDOM":
        adjective=random.choice(adjective_list)

#Verb
    verb=input("Please type in a verb or the word 'random' if you can't decide: ")
    verb=verb.upper()
    if verb=="RANDOM":
        verb=random.choice(verb_list)

#Number
    number=input("Please type in a number or the word 'random' if you can't decide: ")
    number=number.upper()
    if number=="RANDOM":
        number=random.choice(number_list)

#Function
    print(f"""My birthday yesterday was AMAZING. I woke up in the morning and {yellow}{bold1}{verb}{bold2}for HOURS.
After my mom made me breakfeast, I drove to my friend {yellow}{bold1}{name}{bold2}'s house to spend the day with him.
Since we were in Spain, {yellow}{bold1}{name}{bold2} and I decided to go to a soccer game.
It was super fun and the score turned out {yellow}{bold1}{number}{bold1}:0!
After, we were hungry and got some food at {yellow}{bold1}{place}{bold2}.
The food WAS {yellow}{bold1}{adjective}{bold2}! I was so tired after my amazing birthday and went straight to sleep.""")
#Main
madlibs()
