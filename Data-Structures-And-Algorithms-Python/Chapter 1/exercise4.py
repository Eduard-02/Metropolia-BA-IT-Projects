# Exercise
# Sum of the First n Positive Integers
# Write a program that takes a positive integer, n, as input and then displays the sum of
# all of the integers from 1 to n. The sum of the first n positive integers can be computed
# using the formula:

# 𝑠𝑢𝑚=𝑛∗(𝑛+1)/2

n = int(input())

sum = n * (n + 1) / 2

print(f"The sum of the first {n} positive integers is {int(sum)}")