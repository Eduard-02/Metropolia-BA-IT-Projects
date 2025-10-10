#Squares
#Write a program that prints a dictionary where the keys are numbers between 1 and N,
# and the values are square of keys.

n = int(input())

dic = {}
for i in range(1,n + 1):
    dic[i] = i * i
print(dic)
