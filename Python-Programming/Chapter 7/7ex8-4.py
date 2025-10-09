# -*- coding: cp1252 -*-

import inspector

while True:
    userInput = input("Give a string for testing: ")
    tulos = inspector.testme(userInput)

    if tulos == True:
        print("This string fits for a password!")
        break
    else:
        print("The module says no.")
