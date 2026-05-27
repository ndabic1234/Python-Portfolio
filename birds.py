#Birds (CREATE Task)
#The purpose of my program is to help users look at information about a specified bird.
#Init
import webbrowser #Webbrowser is a Python library that allows a URL to be opened from a line of code to your Web Browser
import pandas as pd #This is a Python library that allows Python scripts to read .csv files.

#Functions
data = pd.read_csv('birds.csv') #Imports all csv data to a variable (data)

name = data['Name'].tolist() #Imports all bird names from csv to a variable (name)
scientific_name = data['Scientific Name'].tolist() #Imports all scientific names from csv to an array (scientific_name)
id = data['id'].tolist() #Imports all bird IDs from csv to an array (id)
url = data['Image of Bird'].tolist() #Imports all URLs of pictures of birds to an array (url)
diet = data['Diet'].tolist() #Imports diet of all birds to an array (diet)
primary_color = data['Primary Color'].tolist() #Imports primary color of all birds to an array (primary_color)
conservation = data['Conservation Status'].tolist() #Imports all conservation statuses to an array (conservation)
filter = [] #Creates a filter to sort out information
filter_url = [] #Creates a filter to sort out URLs
filter2 = [] #Secondary filter used to sort out information

def findBird(query): #Prints scientific name and picture of bird provided by query. Query is an input provided by the user
    query = query.title()
    for i in range(len(id)):
        if query in name[i]:
            filter.append(scientific_name[i])
            filter2.append(name[i])
            filter_url.append(url[i])
    try:
        print(f"Here is the scientific name for {filter2[0]}: {filter[0]}. A picture of the bird will also open in your browser.")
        webbrowser.open(filter_url[0])
        print(f"If that wasn't the bird you were looking for, here are other birds with '{query}' in it: {filter2}")
    except:
        print("That bird isn't in our database, maybe try another breed?")
    filter.clear()
    filter2.clear()
    filter_url.clear()

def findStatus(type): #Prints birds in conservation status provided by type. Type is an input provided by the user.
    type = type.title()
    for i in range(len(id)):
        if type in conservation[i]:
            filter.append(name[i])
    try:
        print(f"Here is the list of {type} species: {filter}")
    except:
        print("That isn't a recognized conservation type, maybe try another status?")
    filter.clear()

def findColor(color): #Prints all birds that are a color provided by color. Color is an input provided by the user
    color = color.title()
    for i in range(len(id)):
        if color in primary_color[i]:
            filter.append(name[i])
    try:
        print(f"Here are the animals that are {color}: {filter}")
    except:
        print("No birds of that color are available in our database, maybe try another color?")
    filter.clear()

def findDiet(birdname): #Prints diet of bird provided by birdname. Birdname is an input provided by the user
    birdname = birdname.title()
    for i in range(len(id)):
        if birdname in name[i]:
            filter.append(diet[i])
    try:
        print(f"Here is the diet for the {birdname}: {filter}")
    except:
        print("That bird isn't in our database, maybe try a different bird type?")
    filter.clear()

def main(): #This is the main program that combines all functions
    while True:
        print("Welcome to the Top Bird Lookup service!")
        choice1=input("What would you like to do? 1: to find Scientific Name, 2: to find birds in a Conservation Status, 3: to find birds by Color, 4: to find a bird's diet, or 5: to exit the program: ")
        try:
            if int(choice1) == 1:
                input1 = input("Please type in the typical name of a bird: ")
                findBird(input1)

                final1 = input("Would you like to stay in the program or exit? 1 to continue, 2 to exit: ")
                try:
                    if int(final1) == 1:
                        continue
                    elif int(final1) == 2:
                        break
                except:
                    print("That wasn't recognized, please try again.")
                    continue
            elif int(choice1) == 2:
                input2 = input("Please type in a conservation status (Least Concern, Near Threatened, Vulnerable, Endangered, Critically Endangered): ")
                findStatus(input2)
                final2 = input("Would you like to stay in the program or exit? 1 to continue, 2 to exit: ")
                try:
                    if int(final2) == 1:
                        continue
                    elif int(final2) == 2:
                        break
                except:
                    print("That wasn't recognized, please try again")
                    continue
            elif int(choice1) == 3:
                input3 = input("Please type in a color: ")
                findColor(input3)
                final3 = input("Would you like to stay in the program or exit? 1 to continue, 2 to exit: ")
                try:
                    if int(final3) == 1:
                        continue
                    elif int(final3) == 2:
                        break
                except:
                    print("That wasn't recognized, please try again.")
                    continue
            elif int(choice1) == 4:
                input4 = input("Please enter the name of bird to find their diet: ")
                findDiet(input4)
                final4 = input("Would you like to stay in the program or exit? 1 to continue, 2 to exit: ")
                try:
                    if int(final4) == 1:
                        continue
                    elif int(final4) == 2:
                        break
                except:
                    print("That wasn't recognized, please try again.")
                    continue
            elif int(choice1) == 5:
                break
        except:
            print("That wasn't a recognized option, please try a different option...")
            continue

#Main
main()
#Sources
#100 Birds of the World
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://www.birds.cornell.edu/home/


