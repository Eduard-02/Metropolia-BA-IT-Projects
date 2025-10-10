# Exercise

# Write a function called "custom_encoder" that accepts a string text as parameter and for
# each char of the text it calculates its 0-based position in the following reference string:

# reference_string = 'abcdefghijklmnopqrstuvwxyz'

# The function should return a list that contains all the positions.
# If a char is not found in the reference_string, its position should be -1

def custom_encoder(usr_string):
    my_list = []
    reference_string = 'abcdefghijklmnopqrstuvwxyz'
    for c in usr_string:
        try:
            c = c.lower()
            char_num = reference_string.index(c)
            my_list.append(char_num)
        except ValueError:
            my_list.append(-1)
    return my_list