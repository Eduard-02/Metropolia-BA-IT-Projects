# -*- coding: cp1252 -*-

import random

print("5 coin flips:")

for i in range(0,5):
    num = random.randint(0,1)
    if num == 0:
        print("Tails!")
    elif num == 1:
        print("Heads!")
