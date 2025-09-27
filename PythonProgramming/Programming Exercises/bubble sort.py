# Exercise: Bubble sort
# Make function bubble_sort using bubble sort algorithm to sort numbers given by user;
# order numbers into the ascending order.
# Bubble Sort is the sorting algorithm that works by repeatedly swapping the adjacent elements
# if they are in wrong order.

# Put your code here
def bubble_sort(mylist):
    n = len(mylist)
    for i in range(n-1):
        for j in range(n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
    return mylist

a = []
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element : " %i))
    a.append(value)
print("The Sorted List in Ascending Order : ", bubble_sort(a))

