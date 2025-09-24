# -*- coding: cp1252 -*-

num = input("Give a number: ")

try:
    num = int(num)
except Exception:
    print("The input was malformed.")
else:
    print("The input was suitable!")
