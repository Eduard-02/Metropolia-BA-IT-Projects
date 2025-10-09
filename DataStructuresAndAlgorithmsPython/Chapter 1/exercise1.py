# Exercise: Sort characters
# Write a program that takes a single string as its input and sort its characters from the lowest
# Unicode value to the highest Unicode value. The program should print the new string.


user_string = input("Enter a word: ")
string_list = []

for c in user_string:
    string_list.append(c)

string_list.sort()

print("".join(string_list))