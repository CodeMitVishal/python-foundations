"""Module 3 · Slicing, tuples and sets

SLICING  -> take a part of a list or string:  items[start:stop:step]
TUPLE    -> like a list, but can't be changed: (lat, lon), (name, age)
SET      -> no duplicates, no order, super-fast "is it in here?"

Run it:  python 03_lists_loops/06_slicing_tuples_sets.py
"""

# --- 1. Slicing: [start:stop:step], stop is NOT included -------------------------------
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[0:3])        # ['Mon', 'Tue', 'Wed']   index 0, 1, 2
print(days[:5])         # first 5 (start defaults to 0)
print(days[5:])         # from index 5 to the end: ['Sat', 'Sun']
print(days[-2:])        # the last 2
print(days[::2])        # every 2nd day: ['Mon', 'Wed', 'Fri', 'Sun']
print(days[::-1])       # reversed copy

word = "Python"
print(word[:3], word[-3:], word[::-1])    # Pyt hon nohtyP  (strings slice the same way)

copy = days[:]          # a full slice = a COPY of the list
copy.append("Holiday")
print(len(days), len(copy))               # 7 8  (the original didn't change)

# --- 2. Tuples: fixed groups of values -----------------------------------------------------------
point = (48.37, 10.89)                    # Augsburg's latitude and longitude
lat, lon = point                          # unpack into two variables
print(f"lat={lat}, lon={lon}")
# point[0] = 0  -> TypeError: tuples can't be changed (that's the point!)

def min_max(numbers):
    return min(numbers), max(numbers)     # a function can return a tuple...

low, high = min_max([7, 2, 9, 4])          # ...and you unpack it
print(low, high)                           # 2 9

# --- 3. Sets: unique items -----------------------------------------------------------------------
visitors = ["vishal", "raj", "vishal", "li", "raj"]
unique = set(visitors)
print(len(visitors), "visits from", len(unique), "people:", sorted(unique))

tags = {"python", "beginner"}
tags.add("free")
tags.add("python")                         # already there: nothing happens
print("python" in tags, sorted(tags))      # True ['beginner', 'free', 'python']

python_fans = {"vishal", "raj", "li"}
cloud_fans = {"li", "sam"}
print(sorted(python_fans & cloud_fans))    # in both: ['li']
print(sorted(python_fans | cloud_fans))    # in either: ['li', 'raj', 'sam', 'vishal']
print(sorted(python_fans - cloud_fans))    # only Python fans: ['raj', 'vishal']

# Which one?  list = ordered + changeable, tuple = fixed, set = unique + fast lookups
