# -*- coding: cp1252 -*-

import math

def convert():
    while True:
        num = input("Give a number: ")
        try:
            num = int(num)
        except Exception:
            print("This input is invalid.")
            continue
        else:
            return num

def main():
    option = 0
    print("Calculator")
    while True:
        if (option == 0) or (option == 7):
            num1 = convert()
            num2 = convert()

        print("""(1) +
(2) -
(3) *
(4) /
(5) sin(number1/number2)
(6) cos(number1/number2)
(7) Change numbers
(8) Quit
Current numbers:""", num1, num2)

        option = int(input("Please select something (1-6): "))

        if option == 8:
            print("Thank you!")
            break
        elif option == 1:
            result = num1 + num2
            print("The result is:", result)
        elif option == 2:
            result = num1 - num2
            print("The result is:", result)
        elif option == 3:
            result = num1 * num2
            print("The result is:", result)
        elif option == 4:
            result = num1 / num2
            print("The result is:", result)
        elif option == 5:
            result = math.sin(num1/num2)
            print("The result is:", result)
        elif option == 6:
            result = math.cos(num1/num2)
            print("The result is:", result)
        elif option == 7:
            continue
        else:
            print("Selection was not correct.")

if __name__ == "__main__":
    main()
