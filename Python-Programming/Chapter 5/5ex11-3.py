readFile = open("strings.txt", "r")
content = readFile.readlines()

stringData = ""

for i in range(0, len(content)):
    stringData = str(content[i])

    if stringData[-1] == "\n":
        stringData = stringData[:-1]
    
    validateStr = stringData.isalnum()
    
    if validateStr:
        print(stringData, "was ok.")
    else:
        print(stringData, "was invalid.")

readFile.close()
