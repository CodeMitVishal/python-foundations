"""Module 6 · Demo: company payroll with inheritance

Mixes three kinds of staff in one Company. The payroll loop calls the same
method, monthly_pay(), and each class answers in its own way. This is
called polymorphism.

Run it:  python 06_classes/04_payroll_inheritance.py
"""


# Employee, Manager and Company are the same classes as in files 01 to 03.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary / 12


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def monthly_pay(self):  # override
        base = super().monthly_pay()
        return base + self.bonus / 12


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)

    def payroll(self):
        total = 0
        for e in self.employees:
            total += e.monthly_pay()
        return total


# New in this demo: a third kind of employee.
# Intern only overrides monthly_pay(); everything else comes from Employee.
class Intern(Employee):
    def monthly_pay(self):
        return 1200  # a flat stipend, whatever the salary


acme = Company("Acme")
acme.hire(Employee("Vishal", 60000))
acme.hire(Manager("Li", 90000, 12000))
acme.hire(Intern("Sam", 0))

# Company never changed, yet it handles all three kinds of staff,
# because every one of them has a monthly_pay() method
for e in acme.employees:
    print(e.name, e.monthly_pay())
print("Total:", acme.payroll())   # Total: 14700.0
