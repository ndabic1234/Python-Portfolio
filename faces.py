#Niki
#faces
#In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result.  Be sure to call main at the bottom of your file.
#Functions
def convert(emoji):
    emoji=emoji.replace(":)","🙂")
    emoji=emoji.replace(":(","🙁")
    return emoji
def main():
    feeling=input("Are you feeling happy or sad today? Use :) to show you're happy and :( to show you're sad: ")
    convert_feeling=convert(feeling)
    print(convert_feeling)
#Main
main()
