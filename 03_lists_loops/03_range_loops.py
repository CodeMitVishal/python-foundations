"""Module 3 · Loops with range()

range() produces a sequence of whole numbers. Use it to repeat something a
set number of times, or when you need each item's position.

Run it:  python 03_lists_loops/03_range_loops.py
"""

# range(stop) counts from 0 up to, but NOT including, stop.
# list() turns the range into a list so print() can show every number.
print(list(range(5)))          # [0, 1, 2, 3, 4]
# range(start, stop) begins at start instead of 0
print(list(range(1, 6)))       # [1, 2, 3, 4, 5]
# range(start, stop, step) jumps by step each time
print(list(range(0, 10, 2)))   # [0, 2, 4, 6, 8]
# A negative step counts down
print(list(range(5, 0, -1)))   # [5, 4, 3, 2, 1]

# Repeat 12 times: month takes the values 1, 2, ..., 12
for month in range(1, 13):
    print("Month", month)

# range(len(names)) gives the positions 0, 1, 2,
# so names[i] reads the item at each position
names = ["Vishal", "Raj", "Li"]
for i in range(len(names)):
    print(i, names[i])
