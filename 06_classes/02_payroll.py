"""Module 6 · Demo: company payroll with classes

A Company object holds a list of Employee objects and adds up what it pays
them each month.

Run it:  python 06_classes/02_payroll.py
"""


# Employee is the same class as in 01_employee.py.
# Each file in this folder repeats the classes it needs, so it runs on its own.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary / 12


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []  # starts empty; hire() fills it

    # Objects can hold other objects: here, a list of Employees
    def hire(self, employee):
        self.employees.append(employee)

    # The company doesn't work out anyone's pay itself: it asks each
    # employee for their monthly_pay() and adds up the answers
    def payroll(self):
        total = 0
        for e in self.employees:
            total += e.monthly_pay()
        return total


acme = Company("Acme")
acme.hire(Employee("Vishal", 60000))  # create an Employee and hire them in one line
acme.hire(Employee("Raj", 48000))
print(acme.payroll())   # 9000.0, which is 5000.0 + 4000.0
