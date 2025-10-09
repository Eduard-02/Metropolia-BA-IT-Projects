# -*- coding: cp1252 -*-

readfile = open("words.txt", "r")
mylist = readfile.readlines()

mylist.sort()

print("Words in an alphabetical order:")
for i in mylist:
    print(i[:-1])