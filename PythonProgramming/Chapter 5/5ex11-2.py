fileName = input("Give a file name: ")
content = input("Write something: ")

writeFile = open(fileName,"w")
writeFile.write(content)
writeFile.close()

print("Wrote", content, " to the file", fileName)
