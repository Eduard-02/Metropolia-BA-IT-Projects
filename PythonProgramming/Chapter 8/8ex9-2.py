# -*- coding: cp1252 -*-

fileName = input("Give the file name: ")

try:
    readFile = open(fileName, "r")
    content = readFile.read()
    content = int(content)
    result = 1000 / content
    readFile.close()
except IOError:
    print("There seems to be no file with that name.")
except (TypeError, ValueError):
    print("The file contents were unsuitable.")
except Exception:
    print("There was a problem with the program.")
else:
    print("The result was", result)
