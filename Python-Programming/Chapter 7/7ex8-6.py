# -*- coding: cp1252 -*-

import time

while True:
    print("(1) Read the notebook\n(2) Add note\n\
(3) Empty the notebook\n(4) Quit\n")

    userInp = int(input("Please select one: "))

    if userInp == 1:
        readNotes = open("notebook.txt","r")
        content = readNotes.read()
        print(content)
        readNotes.close()
    elif userInp == 2:
        addNote = open("notebook.txt","a")
        content = input("Write a new note: ")
        dateTime = time.strftime("%X %x")
        addNote.write(content + ":::" + dateTime + "\n")
        addNote.close()
    elif userInp == 3:
        delNotes = open("notebook.txt","w")
        delNotes.close()
        print("Notes deleted.")
    elif userInp == 4:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Invalid input, try again.")
