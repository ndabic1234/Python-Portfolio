#Niki
#grade
#Write a function that asks the user to input a score as an integer and returns the appropriate letter grade (90+ = A, 80+ = B, etc)
#Functions
def letter():
    grade=input("Please enter your grade percentage: ")
    if int(grade) >= 89.5:
        print("A")
    elif int(grade) >= 79.5:
        print("B")
    elif int(grade) >= 69.5:
        print("C")
    elif int(grade) >= 59.5:
        print("D")
    else:
        print("F")

#Main
letter()
