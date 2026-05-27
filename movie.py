#Niki
#Movie
#Write a function that collects the user’s age as input and prints what types of movie the user can see at the movie theatre
#Functions
def movie():
    age = input("Please enter your age: ")
    if int(age) >= 18:
        print("You can watch any movie including Rated-R")
    elif int(age) >= 13:
        print("You can watch PG-13 and PG movies")
    else:
        print("You can only watch PG movies")

#Main
movie()
