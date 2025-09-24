print("Calculator")

num1 = input("Give the first number: ")
num2 = input("Give the second number: ")

print("(1) + \n(2) - \n(3) * \n(4) /")

option = input("Please select something (1-4): ")

if int(option) == 1:
    result = int(num1) + int(num2) # Convert to int so the calculation occurs
    print("The result is: ", result)
elif int(option) == 2:
    result = int(num1) - int(num2)
    print("The result is: ", result)
elif int(option) == 3:
    result = int(num1) * int(num2)
    print("The result is: ", result)
elif int(option) == 4:
    result = int(num1) / int(num2)
    print("The result is: ", result)
else:
    print("Selection was not correct.")
