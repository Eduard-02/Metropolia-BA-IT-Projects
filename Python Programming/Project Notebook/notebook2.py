import time
import pickle

class Notebook:
    def __init__(self, filename = "notebook.dat"):
        self.filename = filename
        self.notes = self.load()

    def load(self):
        try:
            openfile = open(self.filename, "rb")
            noteslist = pickle.load(openfile)
            openfile.close()
            return noteslist
        except IOError:
            print("No default notebook was found, created one.")
            createfile = open(self.filename, "wb")
            noteslist = []
            createfile.close()
        except EOFError:
            pass

    def read(self):
        try:
            for i in self.notes:
                print(i)
        except (EOFError, IOError):
            return []

    def add(self, content):
        addnote = open(self.filename, "wb")
        datetime = time.strftime("%X %x")
        self.notes.append(content + ":::" + datetime)
        pickle.dump(self.notes, addnote)
        addnote.close()

    def edit(self):
        print("The list has", len(self.notes), "notes.")
        notetoedit = int(input("Which of them will be changed?: "))
        try:
            print(self.notes[notetoedit])
            newnote = input("Give the new note: ")
            editnote = open(self.filename, "wb")
            datetime = time.strftime("%X %x")
            self.notes[notetoedit] = newnote + ":::" + datetime
            pickle.dump(self.notes, editnote)
            editnote.close()
        except IndexError:
            print("There is no note in that position.")
        except (ValueError, TypeError):
            print("Invalid input.")

    def delete(self):
        print("The list has", len(self.notes), "notes.")
        notetodel = int(input("Which of them will be deleted?: "))
        try:
            print("Deleted note", self.notes[notetodel])
            self.notes.pop(notetodel)
            delnote = open(self.filename, "wb")
            pickle.dump(self.notes, delnote)
            delnote.close()
        except IndexError:
            print("There is no note in that position.")
        except (ValueError, TypeError):
            print("Invalid input.")

def main():
    nb = Notebook()

    while True:
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
                nb.read()
            elif userinp == 2:
                content = input("Write a new note: ")
                nb.add(content)
            elif userinp == 3:
                nb.edit()
            elif userinp == 4:
                nb.delete()
            elif userinp == 5:
                print("Notebook shutting down, thank you.")
                break

if __name__ == "__main__":
    main()