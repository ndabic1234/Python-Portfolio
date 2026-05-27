#Niki
#playback
#implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ...
#Functions
def playback():
    words=input("Please enter a sentence: ")
    modified=words.replace(" ", "...")
    print(modified)
#Main
playback()
