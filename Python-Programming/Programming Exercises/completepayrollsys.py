def my_split(sentence, sep):
    lst = []
    tmp = ''
    for c in sentence:
        if c == sep:
            lst.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        lst.append(tmp)

    return (lst)

def my_join(lst, sep):
    mystr = ''
    for elem in lst[0:-1]:
        mystr += str(elem) + str(sep)
    mystr += str(lst[-1])

    return (mystr)

class PayrollSystem:
    def calculate_payroll(self, employees):
        for employee in employees:
            print('Employee Payroll')
            print('================')
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_salary()}')
            print('')


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def ask_name(self):
        try:
            self.name = str(input("Please enter employee name:"))
        except:
            self.name = ''


class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.salary = 'M'
        self.monthly_salary = int(monthly_salary)

    def ask_salary(self):
        try:
            self.monthly_salary = int(input("Please enter monthly salary:"))
        except:
            self.monthly_salary = 0

    def calculate_salary(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.salary = 'H'
        self.hours_worked = int(hours_worked)
        self.hour_rate = int(hour_rate)

    def ask_salary(self):
        try:
            self.hours_worked = int(input("Please enter hours worked:"))
            self.hour_rate = int(input("Please enter hour rate:"))
        except:
            self.hours_worked = 0
            self.hour_rate = 0

    def calculate_salary(self):
        return self.hour_rate * self.hours_worked


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, monthly_salary, commission):
        super().__init__(id, name, monthly_salary)
        self.salary = 'C'
        self.monthly_salary = int(monthly_salary)
        self.commission = int(commission)

    def ask_salary(self):
        try:
            self.monthly_salary = int(input("Please enter monthly salary:"))
            self.commission = int(input("Please enter commission:"))
        except:
            self.monthly_salary = 0

    def calculate_salary(self):
        return self.monthly_salary + self.commission

employees = []
id = 1
while True:
    print(
        "(1) Add employee to employees\n(2) Write employees to file\n(3) Read employees from file\n(4) Print payroll\n(0) Quit\n")
    selection = int(input("Please select one: "))
    if selection == 1:
        while True:
            salarytype = int(input("Please enter salary type:\n(1) monthly\n(2) hourly\n(3) commission\n(0) Quit\n"))
            if salarytype == 1:
                employee = SalaryEmployee(id, '', 0)
                SalaryEmployee.ask_name(employee)
                SalaryEmployee.ask_salary(employee)
                employees.append(employee)
                id += 1
            elif salarytype == 2:
                employee = HourlyEmployee(id, '', 0, 0)
                HourlyEmployee.ask_name(employee)
                HourlyEmployee.ask_salary(employee)
                employees.append(employee)
                id += 1
            elif salarytype == 3:
                employee = CommissionEmployee(id, '', 0, 0)
                CommissionEmployee.ask_name(employee)
                CommissionEmployee.ask_salary(employee)
                employees.append(employee)
                id += 1
            elif salarytype == 0:
                break
            else:
                print("Incorrect selection.")

    elif selection == 2:
        openfile = open("employee.csv", "w")
        count = len(employees)
        for employee in employees:
            if employee.salary == "M":
                attrs = [employee.id, employee.name, employee.salary, employee.monthly_salary]
                openfile.write(my_join(attrs, ",") + "\n")
            elif employee.salary == "H":
                attrs = [employee.id, employee.name, employee.salary, employee.hours_worked, employee.hour_rate]
                openfile.write(my_join(attrs, ",") + "\n")
            elif employee.salary == "C":
                attrs = [employee.id, employee.name, employee.salary ,employee.monthly_salary, employee.commission]
                openfile.write(my_join(attrs, ",") + "\n")
        openfile.close()
        print(len(employees), " employee(s) added to employee.csv")

    elif selection == 3:
        readfile = open("employee.csv", "r")
        employees = []
        for line in readfile:
            line = line.strip()
            mylist = my_split(line, ",")
            if mylist[2] == "M":
                mylist[0] = int(mylist[0])
                mylist[3] = int(mylist[3])
                emp = SalaryEmployee(mylist[0], mylist[1], mylist[3])
                employees.append(emp)
            elif mylist[2] == "H":
                mylist[0] = int(mylist[0])
                mylist[3] = int(mylist[3])
                mylist[4] = int(mylist[4])
                emp = HourlyEmployee(mylist[0], mylist[1], mylist[3], mylist[4])
                employees.append(emp)
            elif mylist[2] == "C":
                mylist[0] = int(mylist[0])
                mylist[3] = int(mylist[3])
                mylist[4] = int(mylist[4])
                emp = CommissionEmployee(mylist[0], mylist[1], mylist[3], mylist[4])
                employees.append(emp)
        readfile.close()
        print(len(employees), " employee(s) read from employee.csv")

    elif selection == 4:
        payroll_system = PayrollSystem()
        payroll_system.calculate_payroll(employees)

    elif selection == 0:
        print("Service shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")