#Make class Employee and its initialization method. Employee-class will have 2 attributes: id and name.

#Make program,

# filling the list with objects of Employee class. Id is a serial number from 1 and name will be asked from user.
# ending when user gives '0' instead of a name.
# in the end printing all Employees from list in a format shown in example below.

#You must use: class, def, for

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# Put your code here
emplist = []
id = 1

while True:
    name = input("Please enter employee name (0 to quit):")
    if name == "0":
        break
    employee = Employee(id, name)
    emplist.append(employee)
    id += 1

for employee in emplist:
    print("Id:", employee.id, "Name:", employee.name)
