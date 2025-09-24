# -*- coding: cp1252 -*-

def addproduct(mylist):
    item = input("What will be added?: ")
    if item == "" or item == " ":
        return True
    mylist.append(item)
    return mylist

def removeproduct(mylist):
    print("There are", len(mylist), "items in the list.")
    deleteitem = int(input("Which item is deleted?: "))
    try:
        mylist.pop(deleteitem)
    except IndexError:
        print("Incorrect selection.")
    else:
        return mylist

def endshopping(mylist):
    print("The following items remain in the list:")
    for i in mylist:
        print(i)

def main():
    shoppinglist = []

    while True:
        try:
            selection = int(input("""Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: """))
            if selection == 1:
                addproduct(shoppinglist)
            elif selection == 2:
                removeproduct(shoppinglist)
            elif selection == 3:
                endshopping(shoppinglist)
                break
            else:
                print("Incorrect selection.")
                continue
        except ValueError:
                print("Incorrect selection.")
                continue

if __name__ == "__main__":
    main()