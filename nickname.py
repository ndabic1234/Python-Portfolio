#Niki
#nickname
#Create a program that asks the users this or that questions a generates a name for the user based on the responses.
#Functions
def nickname():
    print("Create your rapper name! To avoid any error, reply to the questions with the exact spelling and capitalization listed.")
    start=input("Do you want your rapper name to start with Lil or Big?: ")
#Lil is beginning
    if start=="Lil":
        print("You've started your rapper name with Lil, move to the next part!")
        middle=input("Do you want the middle of your rapper name to have X or D?: ")
        if middle=="X":
            print("Your rapper name is LilX so far, move on to complete the name!")
            end=input("Do you want your rapper name to end with day or night?: ")
            if end=="day":
                print("Your rapper name is LilXday!")
            elif end=="night":
                print("Your rapper name is LilXnight!")
        elif middle=="D":
            print("Your rapper name is LilD so far, move on to complete the name!")
            end=input("Do you want your rapper name to end with day or night?: ")
            if end=="day":
                print("Your rapper name is LilDday!")
            elif end=="night":
                print("Your rapper name is LilDnight!")

#Big is the beginning
    elif start == "Big":
        print("You've started your rapper name with Big, move to the next part!")
        middle=input("Do you want the middle of your rapper name to have X or D?: ")
        if middle=="X":
            print("Your rapper name is BigX so far, move on to complete the name!")
            end=input("Do you want your rapper name to end with day or night?: ")
            if end=="day":
                print("Your rapper name is BigXday!")
            elif end=="night":
                print("Your rapper name is BigXnight!")

        elif middle=="D":
            print("Your rapper name is BigD so far, move on to complete the name!")
        end=input("Do you want your rapper name to end with day or night?: ")
        if end=="day":
            print("Your rapper name is BigDday!")
        elif end=="night":
            print("Your rapper name is BigDnight!")
#Main
nickname()
