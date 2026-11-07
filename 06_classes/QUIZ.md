# Python Foundations – Module 6 Knowledge Check
**Classes and Objects**

Try to answer without rewatching. The answer key with video timestamps is at the bottom.

---

### Part A – Multiple choice

**1. What is a class?**
- A) A variable that stores one value
- B) A user-defined data type: a blueprint for objects
- C) A built-in function
- D) A file of code

**2. What is an object?**
- A) An instance of a class with its own values
- B) Another name for a function
- C) A type of loop
- D) A module you import

**3. When does `__init__` run?**
- A) When you import the file
- B) When you call any method
- C) When you create a new object
- D) When the program ends

**4. What is `self`?**
- A) The class itself
- B) The object the method is working on
- C) A global variable
- D) A Python keyword you must import

**5. Every object has three things. Which list is correct?**
- A) Name, size, colour
- B) Identity (`id`), type (class), state (attribute values)
- C) Stack, heap, code
- D) Key, value, index

**6. Where does Python store the objects you create?**
- A) On the stack
- B) On the heap
- C) In the code area
- D) In a file

**7. What does a variable like `vishal` hold?**
- A) A full copy of the object
- B) A reference to the object on the heap
- C) The object's code
- D) Nothing until you print it

**8. Where are a class's methods (their code) kept?**
- A) Once, in the code area, shared by all objects
- B) A separate copy inside every object
- C) On the stack
- D) Only in the `.py` file, not in memory

**9. `b = a` where `a` is an object. What happens?**
- A) A new copy of the object is made
- B) `b` refers to the same object as `a`
- C) `a` is deleted
- D) It's an error

**10. What does `a is b` check?**
- A) Whether `a` and `b` have equal values
- B) Whether `a` and `b` are the same object
- C) Whether `b` is a subclass of `a`
- D) Whether `a` is not `None`

**11. What does `del a` do?**
- A) Deletes the object immediately, even if `b` still refers to it
- B) Removes the name `a`; the object is freed only when nothing refers to it
- C) Empties the object's attributes
- D) Deletes the class

**12. How do you make `Manager` inherit from `Employee`?**
- A) `class Manager inherits Employee:`
- B) `class Manager(Employee):`
- C) `class Manager extends Employee:`
- D) `class Manager = Employee:`

**13. What does `super().__init__(name, salary)` do inside `Manager`?**
- A) Creates a second object
- B) Calls the parent's `__init__` to reuse its setup
- C) Deletes the parent class
- D) Makes the method private

**14. What is method overriding?**
- A) Defining a method with the same name in the child class to change its behaviour
- B) Calling a method twice
- C) Deleting a method from the parent
- D) Giving a method two different parameter lists

---

### Part B – What's the output?

**15.** What is printed?
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        return self.salary / 12

vishal = Employee("Vishal", 60000)
print(vishal.name, vishal.monthly_pay())
```

**16.** What is printed?
```python
a = Employee("Vishal", 60000)
b = a
c = Employee("Vishal", 60000)
b.salary = 70000
print(a.salary, a is b, a is c)
```

**17.** What is printed?
```python
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def monthly_pay(self):
        return super().monthly_pay() + self.bonus / 12

boss = Manager("Li", 96000, 12000)
print(boss.monthly_pay(), isinstance(boss, Employee))
```

---

### Part C – Fix the bug

**18.** This crashes with `TypeError: Employee.monthly_pay() takes 0 positional arguments but 1 was given`. Fix it.
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay():
        return self.salary / 12
```

**19.** `Manager` objects have no `name` attribute (`AttributeError`). Fix it.
```python
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        self.bonus = bonus
```

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Explanation | Video |
|---|--------|-------------|-------|
| 1 | B | A class is a blueprint that defines attributes and methods. | 1:57 |
| 2 | A | An object is an instance built from the class. | 2:26 |
| 3 | C | `__init__` sets up a new object's attributes. | 1:37 |
| 4 | B | `self` is the object itself; every method gets it first. | 1:37 |
| 5 | B | Identity, type and state. | 2:37 |
| 6 | B | Objects live on the heap. | 3:35 |
| 7 | B | Names on the stack hold references to heap objects. | 6:23 |
| 8 | A | Method code is stored once and shared. | 3:35 |
| 9 | B | `=` copies the reference, not the object. | 8:02 |
| 10 | B | `is` compares identity; `==` compares values. | 7:49 |
| 11 | B | `del` removes the name; garbage collection frees unused objects. | 9:15 |
| 12 | B | Put the parent class in brackets. | 12:50 |
| 13 | B | `super()` calls the parent's version. | 13:24 |
| 14 | A | Redefine a method with the same name in the child. | 13:24 |
| 15 | `Vishal 5000.0` | `60000 / 12` is `5000.0`. | 0:26 |
| 16 | `70000 True False` | `a` and `b` are one object; `c` is another one. | 8:02 |
| 17 | `9000.0 True` | `96000/12 + 12000/12`; a Manager is also an Employee. | 13:18 |
| 18 | Add `self`: `def monthly_pay(self):` | Every method gets the object as its first parameter. | 1:37 |
| 19 | Add `super().__init__(name, salary)` as the first line. | Reuse the parent's setup to set `name` and `salary`. | 13:24 |

</details>

---

If this module helped you, you can support the channel:

- **Buy me a coffee** at [buymeacoffee.com/the_growthclub](https://buymeacoffee.com/the_growthclub) ☕
- **Subscribe** to [The Growth Club](https://www.youtube.com/@TheGrowthClubOfficial) on YouTube
- **Star** this repo so others can find it

Every coffee helps me keep making free Python lessons. Thank you! 🙏
