# -*- coding: cp1252 -*-

class Player:
    teamColor = "Blue"
    __points = 0

    def tellscore(self):
        print("I am", self.teamColor + ",", "we have", self.__points, "points!")

    def goal(self):
        self.__points += 1


def main():
    gamer = Player()

    gamer.goal()
    gamer.tellscore()

if __name__ == "__main__":
    main()