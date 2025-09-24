num_1 = input("Give a number: ")
num_2 = input("Give another number: ")

if ((int(num_1) % 2) == 0) and ((int(num_2) % 2) == 0):
    print("Both numbers are even.")
elif ((int(num_1) % 2) == 0) or ((int(num_2) % 2) == 0):
    print("One of the numbers is even.")
elif ((int(num_1) % 2) != 0) and ((int(num_2) % 2) != 0):
    print("Both numbers are odd.")
