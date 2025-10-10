# Exercise:
# Sum a Collection of Numbers
# Write a program that sums all of the numbers taken as input, while ignoring any input that is not a
# valid number.
# Your program should display the current sum after each number is entered. It should display
# an error message after each non-numeric input, and then continue to sum any additional numbers
# entered by the user.  The program exits when the user enters 0.
# Ensure that your program works correctly for both integers and floating-point numbers.

sum = 0
while True:
    try:
        n = float(input())
        if n == 0:
            print(f"The grand total is {sum}")
            break
        sum = sum + n
        print(f"The total is now {sum}")
    except (ValueError, TypeError):
        print("That wasn’t a number.")
        continue