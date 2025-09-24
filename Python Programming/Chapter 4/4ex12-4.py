option = 0
print("Calculator")
while True:
    if (option == 0) or (option == 5):
        num1 = int(input("Give the first number: "))
        num2 = int(input("Give the second number: "))

    print("(1) + \n(2) - \n(3) * \n(4) / \n\
(5) Change numbers \n(6) Quit \n\
Current numbers:", str(num1), str(num2))

    option = int(input("Please select something (1-6): "))

    if option == 6:
        print("Thank you!")
        break
    elif option == 1:
        result = num1 + num2 # Convert to int so the calculation occurs
        print("The result is: ", result)
    elif option == 2:
        result = num1 - num2
        print("The result is: ", result)
    elif option == 3:
        result = num1 * num2
        print("The result is: ", result)
    elif option == 4:
        result = num1 / num2
        print("The result is: ", result)
    elif option == 5:
        continue
    else:
        print("Selection was not correct.")
