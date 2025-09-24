def tester(givenstring = "Too short"):
    if len(givenstring) < 10:
        print(givenstring)
    elif len(givenstring) >= 10:
        print(givenstring)

        for i in range(0, len(givenstring)):
            if givenstring[i] == "X":
                return True

def main():
    while True:
        userIn = input("Write something (quit ends): ")
        
        if userIn == "quit":
            break
        
        if len(userIn) < 10:
            tester()
            continue
        
        if tester(userIn):
            print("X spotted!")
        
if __name__ == "__main__":
    main()
