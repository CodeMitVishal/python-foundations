"""Module 5 · Functions

A function is a named block of code you can run (call) whenever you need
it. You pass values in as arguments, and return sends a result back.

Run it:  python 05_functions/01_functions.py
"""


# def starts a function: its name, then its parameters in ( ).
# greeting="Hello" is a default value, used when the caller leaves it out.
def greet(name, greeting="Hello"):
    """Return a friendly greeting."""
    message = f"{greeting}, {name}!"
    return message  # send the result back to whoever called greet()


# The body only runs when you call the function
print(greet("Vishal"))                         # Hello, Vishal!  (default greeting)
print(greet("Raj", "Hi"))                   # Hi, Raj!     (arguments by position)
print(greet(greeting="Hey", name="Li"))     # Hey, Li!     (by name, any order)


# A function with no return gives back None
def say_hi():
    print("hi")


result = say_hi()  # prints "hi", but returns nothing
print(result)   # None

# message was created inside greet(), so it only exists there (local scope).
# This line would fail:
# print(message)   # NameError
