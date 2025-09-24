# -*- coding: cp1252 -*-

import time
import pickle

def addnotefunc(currentnb, noteslist, content):
    addnote = open(currentnb, "wb")
    datetime = time.strftime("%X %x")
    noteslist.append(content + ":::" + datetime)
    pickle.dump(noteslist, addnote)
    addnote.close()

def editnotefunc(currentnb, noteslist):
    print("The list has", len(noteslist), "notes.")
    notetoedit = int(input("Which of them will be changed?: "))
    try:
        print(noteslist[notetoedit])
        newnote = input("Give the new note: ")
        editnote = open(currentnb, "wb")
        datetime = time.strftime("%X %x")
        noteslist[notetoedit] = newnote + ":::" + datetime
        pickle.dump(noteslist, editnote)
        editnote.close()
    except IndexError:
        print("There is no note in that position.")
    except (ValueError, TypeError):
        print("Invalid input.")

def deletenotefunc(currentnb, noteslist):
    print("The list has", len(noteslist), "notes.")
    notetodel = int(input("Which of them will be deleted?: "))
    try:
        print("Deleted note", noteslist[notetodel])
        noteslist.pop(notetodel)
        delnote = open(currentnb, "wb")
        pickle.dump(noteslist, delnote)
        delnote.close()
    except IndexError:
        print("There is no note in that position.")
    except (ValueError, TypeError):
        print("Invalid input.")

def readnotefunc(currentnb):
    try:
        readnotes = open(currentnb, "rb")
        noteslist = pickle.load(readnotes)
        for i in noteslist:
            print(i)
        readnotes.close()
    except EOFError:
        pass

def main():
    currentnb = "notebook.dat"
    noteslist = []

    while True:
        try:
            openfile = open(currentnb, "rb")
            noteslist = pickle.load(openfile)
            openfile.close()
        except IOError:
            print("No default notebook was found, created one.")
            createfile = open(currentnb, "wb")
            noteslist = []
            createfile.close()
        except EOFError:
            pass

        print("""(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit
    """)

        userinp = input("Please select one: ")

        try:
            userinp = int(userinp)
        except (TypeError, ValueError):
            print("Invalid input, try again.")
        else:
            if userinp == 1:
                readnotefunc(currentnb)
            elif userinp == 2:
                content = input("Write a new note: ")
                addnotefunc(currentnb, noteslist, content)
            elif userinp == 3:
                editnotefunc(currentnb, noteslist)
            elif userinp == 4:
                deletenotefunc(currentnb, noteslist)
            elif userinp == 5:
                print("Notebook shutting down, thank you.")
                break

if __name__ == "__main__":
    main()