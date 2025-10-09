# Exercise
# In this exercise create two functions

#   my_split : which splits sentence given as first argument using second argument as a separator character to separate list items. Function returns a list of items.

#   my_join : which joins list given as first argument to a string separated with character given as second argument. Function returns a string.

# In this exercise you are not allowed to use Python split and join functions

def my_split(sentence, space=" "):
    word = ""
    mylist = []
    for char in sentence:
        if char == space:
            mylist.append(word)
            word = ""
        else:
            word = word + char
    mylist.append(word)
    return mylist


def my_join(mylist, sepa=" "):
    sentence = ""
    for i in mylist:
        if i == mylist[0]:
            sentence = sentence + i
        else:
            sentence = sentence + sepa + i
    return sentence


sentence = str(input("Please enter sentence:"))
print(my_join(my_split(sentence, ' '), ','))
print(my_join(my_split(sentence, ' '), '\n'))