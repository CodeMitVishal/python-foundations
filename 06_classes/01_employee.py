"""Module 6 · Classes

A class is a blueprint. Each object made from it (an instance) has its own
data, called attributes, and can do things, through methods.

Run it:  python 06_classes/01_employee.py
"""


# class starts the blueprint; class names use CapitalWords
class Employee:
    # __init__ runs automatically when you create an Employee.
    # self is the new object itself; name and salary are passed in.
    def __init__(self, name, salary):
        self.name = name        # store the values on the object
        self.salary = salary    # as its attributes

    # A method is a function that belongs to the class.
    # It reads the object's own data through self.
    def monthly_pay(self):
        return self.salary / 12


# Calling the class creates objects: two employees from one blueprint
vishal = Employee("Vishal", 60000)
raj = Employee("Raj", 48000)
print(vishal.name)          # Vishal: read an attribute with a dot
print(vishal.monthly_pay())  # 5000.0
print(raj.monthly_pay())    # 4000.0: the same method, using Raj's data
