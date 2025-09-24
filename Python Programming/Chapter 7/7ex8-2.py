# -*- coding: cp1252 -*-

import random

def checkWin(user, cp):
    if (user == "Foot" and cp == "Cockroach") \
        or (user == "Nuke" and cp == "Foot") \
        or (user == "Cockroach" and cp == "Nuke"):
        print("You WIN!")
        return True
    elif user == cp:
        print("It is a tie!")
        return False
    else:
        print("You LOSE!")

def main():
    rounds = 0
    roundsWon = 0
    ties = 0

    while True:
        userIn = input("Foot, Nuke or Cockroach? (Quit ends): ")

        cpIn = random.randint(1,3)

        if userIn == "Quit":
            print("You played", rounds, "rounds, and won", roundsWon, "rounds,\
 playing tie in", ties, "rounds.")
            break
        elif userIn not in ("Foot", "Nuke", "Cockroach"):
            print("Incorrect selection.")
            continue

        if cpIn == 1:
            cpIn = "Foot"
        elif cpIn == 2:
            cpIn = "Nuke"
        elif cpIn == 3:
            cpIn = "Cockroach"

        print("You chose:", userIn)
        print("Computer chose:", cpIn)

        check = checkWin(userIn, cpIn)
        
        if check == True:
            roundsWon += 1
        elif check == False:
            ties += 1
        rounds += 1

if __name__ == "__main__":
    main()
