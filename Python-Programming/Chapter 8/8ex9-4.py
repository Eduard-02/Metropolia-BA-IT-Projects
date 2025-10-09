# -*- coding: cp1252 -*-

import time

currentNb = "notebook.txt"

while True:
    try:
        openFile = open(currentNb, "r")
        openFile.close()
    except IOError:
        print("No default notebook was found, created one.")
        createFile = open(currentNb, "w")
        createFile.close()
    
    print("""Now using file""", currentNb, """
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit
""")
    
    userInp = input("Please select one: ")

    try:
        userInp = int(userInp)
    except (TypeError, ValueError):
        print("Invalid input, try again.")
    else:
        if userInp == 1:
            readNotes = open(currentNb,"r")
            content = readNotes.read()
            print(content)
            readNotes.close()
            
        elif userInp == 2:
            addNote = open(currentNb,"a")
            content = input("Write a new note: ")
            dateTime = time.strftime("%X %x")
            addNote.write(content + ":::" + dateTime + "\n")
            addNote.close()
            
        elif userInp == 3:
            delNotes = open(currentNb,"w")
            delNotes.close()
            print("Notes deleted.")

        elif userInp == 4:
            currentNb = input("Give the name of the new file: ")
            try:
                openFile = open(currentNb, "r")
                openFile.close()
            except IOError:
                print("No notebook with that name detected, created one.")
                createFile = open(currentNb, "w")
                createFile.close()
            
        elif userInp == 5:
            print("Notebook shutting down, thank you.")
            break
