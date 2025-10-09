def tester(givenstring = "Too short"):
    print(givenstring)

def main():
    while True:
        userIn = input("Write something (quit ends): ")
        
        if userIn == "quit":
            break
        elif len(userIn) < 10:
            tester()          
        elif len(userIn) > 10:
            tester(userIn)
        
if __name__ == "__main__":
    main()
