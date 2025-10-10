# Exercise
# Count vowels
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

s = input()
n = 0

for c in s:
    if c in ("a","e","i","o","u"):
        n += 1
print(f"Number of vowels: {n}")