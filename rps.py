#Init
#Niki
#rps
#In this programming assignment, you will create a simple Python program that allows the player to play the classic game of "Rock-Paper-Scissors" against the computer.
import random
import time
def rps():
    win=0
    loss=0
    tie=0
    while True:
        comp=random.randint(1,3)
        print("Welcome to Rock-Paper-Scissors. You will be playing against the computer.")
        move=input("Please type in either rock, paper, scissors, or exit to leave the game: ")
        move=move.lower()
        time.sleep(0.5)
        if move=="rock" and comp==1:
            tie=tie+1
            print(f"Tie. wins={win} losses={loss} ties={tie}")
        elif move=="rock" and comp==2:
            loss=loss+1
            print(f"Computer wins. wins={win} losses={loss} ties={tie}")
        elif move=="rock" and comp==3:
            win=win+1
            print(f"Player wins. wins={win} losses={loss} ties={tie}")
        elif move=="paper" and comp==1:
            win=win+1
            print(f"Player wins. wins={win} losses={loss} ties={tie}")
        elif move=="paper" and comp==2:
            tie=tie+1
            print(f"Tie. wins={win} losses={loss} ties={tie}")
        elif move=="paper" and comp==3:
            loss=loss+1
            print(f"Computer wins. wins={win} losses={loss} ties={tie}")
        elif move=="scissors" and comp==1:
            loss=loss+1
            print(f"Computer wins. wins={win} losses={loss} ties={tie}")
        elif move=="scissors" and comp==2:
            win=win+1
            print(f"Player wins. wins={win} losses={loss} ties={tie}")
        elif move=="scissors" and comp==3:
            tie=tie+1
            print(f"Tie. wins={win} losses={loss} ties={tie}")
        elif move=="exit":
            break
        else:
            print("Error. Please retype your answer.")

#Functions
rps()
