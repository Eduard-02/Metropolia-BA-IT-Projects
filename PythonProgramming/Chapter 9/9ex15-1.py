# -*- coding: cp1252 -*-

class Player:
    teamColor = ""
    points = 0

def main():
    gamer = Player()

    gamer.teamColor = "Blue"
    gamer.points = 300

    print("The", gamer.teamColor, "contender has", gamer.points, "points!")

if __name__ == "__main__":
    main()