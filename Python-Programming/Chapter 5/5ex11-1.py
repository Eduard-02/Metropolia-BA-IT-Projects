readfile = open("facts.txt","r")
content = readfile.read()
readfile.close()

print("Following was read from the file:", content)
