"""Module 4 · Combining lists and dictionaries

Real data is often nested: a list of dictionaries (many records with the
same shape) or a dictionary of lists (values grouped under a key).

Run it:  python 04_dicts_json_pip/03_lists_and_dicts.py
"""

# A list of dictionaries: many records with the same shape
people = [
    {"name": "Vishal", "age": 31},
    {"name": "Raj", "age": 27},
]
# Read nested access left to right: people[1] is Raj's dictionary,
# then ["name"] reads the name from it
print(people[1]["name"])  # Raj

# In this loop, person is one whole dictionary at a time
for person in people:
    print(person["name"])

# A dictionary of lists: values grouped under a key
grades = {
    "math": [90, 85],
    "art": [70, 95, 88],
}
# grades["art"] is a list, then [0] is that list's first item
print(grades["art"][0])   # 70

# grades["math"] is a list, so list methods like append() work on it
grades["math"].append(77)
print(grades)
