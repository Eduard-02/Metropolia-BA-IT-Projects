# Exercise
# In this exercise we will extend Class Employee with HourlyEmployee and CommissionEmployee subclasses.

# Define HourlyEmployee as a subclass of Employee class:
#   Write method ask_salary, which is used to query hour_rate and hours_worked attributes from the user.
#   Write method calculate_salary, which is used to calculate salary using: hour_rate * hours_worked.

#Define CommissionEmployee as a subclass of SalaryEmployee (which is a subclass of Employee).
#   Write method ask_salary, which is used to query commission from the user.
#   Write method calculate_salary, which is used to calculate salary using: monthly_salary + commission.

# Payroll is printed using Class PayrollSystem.

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


# My code starts here

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

# My code ends here

employees = []
id = 1
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

payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)