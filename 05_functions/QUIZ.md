# Python Foundations – Module 5 Knowledge Check
**Functions**

Try to answer without rewatching. The answer key with video timestamps is at the bottom.

---

### Part A – Multiple choice

**1. What is a function?**
- A) A variable that stores many values
- B) A named block of code that does one job
- C) A type of loop
- D) A file you import

**2. Which keyword defines a function?**
- A) `function`
- B) `func`
- C) `def`
- D) `define`

**3. In `def greet(name, greeting="Hello"):`, what is `name`?**
- A) A parameter
- B) A return value
- C) A global variable
- D) A module

**4. In the same function, what does `greeting="Hello"` mean?**
- A) `greeting` must always be `"Hello"`
- B) `greeting` is optional and is `"Hello"` if you don't pass it
- C) `greeting` is a constant
- D) It's a syntax error

**5. What does `return` do?**
- A) Prints a value on screen
- B) Ends the program
- C) Sends a value back to the caller
- D) Restarts the function

**6. What does a function return if it has no `return` statement?**
- A) `0`
- B) `""`
- C) `False`
- D) `None`

**7. Which call uses keyword arguments?**
- A) `greet("Raj", "Hi")`
- B) `greet(greeting="Hi", name="Raj")`
- C) `greet["Raj"]`
- D) `greet.Raj("Hi")`

**8. A variable created inside a function is used outside it. What happens?**
- A) It works normally
- B) It returns `None`
- C) `NameError`, because the variable only exists inside the function (local scope)
- D) Python creates it automatically

**9. Why use functions?**
- A) They make programs run on more computers
- B) Code is shorter, not repeated, and easier to read and test
- C) Python requires them
- D) They replace loops

**10. `def roll_die(sides=6):` What does `roll_die()` use for `sides`?**
- A) `0`
- B) `1`
- C) `6`
- D) An error, because `sides` is missing

---

### Part B – What's the output?

**11.** What is printed?
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Vishal"))
print(greet("Raj", "Hi"))
```

**12.** What is printed?
```python
def say_hi():
    print("hi")

result = say_hi()
print(result)
```

**13.** What is printed?
```python
def add(a, b):
    return a + b

print(add(2, 3) * 10)
```

---

### Part C – Fix the bug

**14.** This should print `25`, but it prints `None`. Fix it.
```python
def square(n):
    print(n * n)

result = square(5)
print(result)
```

**15.** This crashes with `NameError: name 'message' is not defined`. Fix it.
```python
def make_message(name):
    message = "Hello, " + name

make_message("Vishal")
print(message)
```

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Explanation | Video |
|---|--------|-------------|-------|
| 1 | B | A function is a named block of code that does one job. | 0:24 |
| 2 | C | `def` starts a function definition. | 0:46 |
| 3 | A | `name` is a parameter: the value you pass in. | 0:46 |
| 4 | B | A default value makes the parameter optional. | 1:00 |
| 5 | C | `return` sends the result back to whoever called the function. | 1:18 |
| 6 | D | Without `return`, a function gives back `None`. | 3:19 |
| 7 | B | Naming each argument (`name=...`) makes it a keyword argument; order doesn't matter. | 1:50 |
| 8 | C | Variables inside a function have local scope. | 2:00 |
| 9 | B | Write once, run anywhere: shorter, no repetition, easier to test. | 0:38 |
| 10 | C | The default `sides=6` is used when nothing is passed. | 6:23 |
| 11 | `Hello, Vishal!` then `Hi, Raj!` | The first call uses the default greeting. | 1:31 |
| 12 | `hi` then `None` | `say_hi()` prints, but returns nothing. | 3:19 |
| 13 | `50` | `add(2, 3)` returns `5`, then `5 * 10`. | 1:18 |
| 14 | Replace `print(n * n)` with `return n * n`. | `print` only shows a value; `return` gives it back. | 1:18 |
| 15 | Add `return message` and use `message = make_message("Vishal")` before printing. | Use `return` to get a value out of a function's scope. | 2:00 |

</details>

---

If this module helped you, you can support the channel:

- **Buy me a coffee** at [buymeacoffee.com/the_growthclub](https://buymeacoffee.com/the_growthclub) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it

Every coffee helps me keep making free Python lessons. Thank you! 🙏
