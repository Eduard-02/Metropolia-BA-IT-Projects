userNum = int(input("Give a number: "))
result = 0

for i in range(userNum):
    result = result + i
    i += 1

print("The sum was: ", int(result))
