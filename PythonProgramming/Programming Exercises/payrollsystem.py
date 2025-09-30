# Exercise: PayrollSystem

# Define first classes

#   1. PayrollSystem, having method calculate_payroll and getting a list of employees as a parameter. Method should calculate and print payroll for employees.
#   2. SalaryEmployee, a subclass of Employee. SalaryEmployee has its own attribute monthly_salary and method calculate_salary, which will return the monthly salary of an employee.

# Finally make then program,
#   asking employee name as in previous Employee-exercise and also asking monthly salary for SalaryEmployee-class.
#   creating SalaryEmployee-objects and store them into a list.
#   ending when user gives '0' instead of a name.
#   using at the end PayrollSystem to print Payroll for Employees in a format shown in the example below.

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

class PayrollSystem:
    def __init__(self, mylist):
        self.mylist = mylist

    def calculate_payroll(self):
        for employee in self.mylist:
            print("""Employee Payroll
================""")
            print("Payroll for:", employee.emp_id, "-", employee.name)
            print("- Check amount: ", employee.monthly_salary, "\n", sep="")

class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        self.emp_id = emp_id
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

def main():
    emp_list = []
    emp_id = 1

    while True:
        name = input("Please enter employee name (0 to quit):")
        if name == "0":
            payroll = PayrollSystem(emp_list)
            payroll.calculate_payroll()
            break
        salary = int(input("Please enter salary:"))
        salaryemployee = SalaryEmployee(emp_id, name, salary)
        emp_list.append(salaryemployee)
        emp_id += 1

if __name__ == "__main__":
    main()