# -*- coding: cp1252 -*-

def testme(password):
    if len(password) < 6 or password.isalpha() or password.isdigit():
        return False
    else:
        return True
