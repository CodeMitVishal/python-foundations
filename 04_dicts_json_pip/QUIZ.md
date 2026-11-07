# Python Foundations – Module 4 Knowledge Check
**Dictionaries, JSON & pip**

Try to answer without rewatching. The answer key with video timestamps is at the bottom.

---

### Part A – Multiple choice

**1. How do you create a dictionary in Python?**
- A) `["title", "Inception"]`
- B) `{"title": "Inception"}`
- C) `("title": "Inception")`
- D) `<"title" = "Inception">`

**2. `movie = {"title": "Inception", "year": 2010}`. How do you read the year?**
- A) `movie[1]`
- B) `movie.year`
- C) `movie["year"]`
- D) `movie(year)`

**3. What happens with `movie["director"]` if the key `"director"` does not exist?**
- A) It returns `None`
- B) It returns an empty string
- C) It raises a `KeyError`
- D) It adds the key

**4. What does `movie.get("director", "?")` return if the key is missing?**
- A) `"?"`
- B) `None`
- C) A `KeyError`
- D) `False`

**5. How do you add a new key `genre` to `movie`?**
- A) `movie.append("genre", "sci-fi")`
- B) `movie["genre"] = "sci-fi"`
- C) `movie.add("genre": "sci-fi")`
- D) `movie + {"genre": "sci-fi"}`

**6. Which statement about dictionary keys is true?**
- A) Keys can repeat
- B) Keys are always numbers
- C) Keys are unique
- D) Keys must be in alphabetical order

**7. What does `"year" in movie` check?**
- A) Whether `"year"` is one of the values
- B) Whether `"year"` is one of the keys
- C) Whether the dictionary is empty
- D) Nothing, it is a syntax error

**8. Which method lets you loop over keys and values together?**
- A) `movie.items()`
- B) `movie.pairs()`
- C) `movie.all()`
- D) `movie.entries()`

**9. What is JSON?**
- A) A Python package you install with pip
- B) A text format for storing and sending data
- C) A kind of database
- D) Another name for a Python dictionary

**10. Which pair is correct (JSON → Python)?**
- A) `null` → `None`
- B) `true` → `"true"`
- C) `array` → `dict`
- D) `object` → `list`

**11. Which function turns a JSON *string* into a dictionary?**
- A) `json.dumps()`
- B) `json.load()`
- C) `json.loads()`
- D) `json.read()`

**12. What is pip used for?**
- A) Running Python files
- B) Installing extra packages from PyPI
- C) Formatting code
- D) Creating dictionaries

**13. Which command creates a virtual environment in a folder called `.venv`?**
- A) `pip install venv`
- B) `python -m venv .venv`
- C) `python venv create`
- D) `pip venv .venv`

**14. What does `pip freeze > requirements.txt` do?**
- A) Stops pip from installing packages
- B) Deletes all installed packages
- C) Saves the list of installed packages to a file
- D) Upgrades pip

---

### Part B – What's the output?

**15.** What is printed?
```python
movie = {"title": "Inception", "rating": 8.8}
movie["rating"] = 9.0
movie["genre"] = "sci-fi"
print(len(movie), movie["rating"])
```

**16.** What is printed?
```python
people = [{"name": "Vishal", "age": 31}, {"name": "Raj", "age": 27}]
print(people[1]["name"])
```

**17.** What is printed?
```python
grades = {"vishal": [90, 85], "raj": [70]}
grades["raj"].append(88)
print(grades["raj"])
```

**18.** What is printed?
```python
import json
data = json.loads('{"name": "Vishal", "langs": ["Python", "SQL"]}')
print(data["langs"][0])
```

---

### Part C – Fix the bug

**19.** This code crashes with `KeyError: 'Batman'`. Make it print "Not showing today" instead.
```python
schedule = {"Dune": ["17:00", "20:00"]}
movie = "Batman"
print(schedule[movie])
```

**20.** You ran `pip install requests`, but `import requests` still fails with `ModuleNotFoundError`. What is the most likely cause?

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Explanation | Video |
|---|--------|-------------|-------|
| 1 | B | Curly braces with `key: value` pairs make a dictionary. | 0:24 |
| 2 | C | You read a value by passing its key in square brackets. | 0:42 |
| 3 | C | Square brackets raise `KeyError` when the key is missing. | 1:17 |
| 4 | A | `get()` returns the default you pass when the key is missing. | 1:17 |
| 5 | B | Assigning to a new key adds it. | 0:55 |
| 6 | C | Keys are always unique; assigning again overwrites the value. | 2:02 |
| 7 | B | `in` checks the keys, not the values. | 2:07 |
| 8 | A | `items()` gives `(key, value)` pairs. | 1:32 |
| 9 | B | JSON is a text format used by files, websites and APIs. | 12:32 |
| 10 | A | JSON `null` becomes Python `None`. | 12:59 |
| 11 | C | `loads` = load from a string; `load` reads a file. | 13:44 |
| 12 | B | pip installs packages other people wrote, from PyPI. | 17:11 |
| 13 | B | `python -m venv .venv` creates the environment. | 18:06 |
| 14 | C | `freeze` lists installed packages; `>` saves them to the file. | 18:23 |
| 15 | `3 9.0` | Three keys after adding `genre`; rating was updated. | 0:49 |
| 16 | `Raj` | Index `[1]` picks the second dictionary, then `["name"]`. | 7:04 |
| 17 | `[70, 88]` | The value is a list, so `append()` works on it. | 6:19 |
| 18 | `Python` | `loads` gives a dict; `langs` is a list, `[0]` is the first item. | 14:07 |
| 19 | Use `if movie in schedule:` … `else: print("Not showing today")` (or `schedule.get(movie)`). | Check the key before reading it. | 4:09 |
| 20 | The virtual environment isn't active, or VS Code uses another interpreter. | Activate `.venv` (or pick it as the interpreter) and run again. | 19:51 |

</details>

---

If this module helped you, you can support the channel:

- **Buy me a coffee** at [buymeacoffee.com/the_growthclub](https://buymeacoffee.com/the_growthclub) ☕
- **Subscribe** to [The Growth Club](https://www.youtube.com/@TheGrowthClubOfficial) on YouTube
- **Star** this repo so others can find it

Every coffee helps me keep making free Python lessons. Thank you! 🙏
