# Python Foundations – Module 7 Knowledge Check
**Working with Files and Exceptions**

Try to answer without rewatching. The answer key with video timestamps is at the bottom.

---

### Part A – Multiple choice

**1. What is an exception?**
- A) A mistake in how the code is written, found before it runs
- B) An error that happens while the program is running
- C) A comment in the code
- D) A type of loop

**2. What happens if nobody catches an exception?**
- A) Python ignores it
- B) The program stops and shows a traceback
- C) The line is skipped
- D) Python fixes it automatically

**3. Which exception does `int("abc")` raise?**
- A) `TypeError`
- B) `KeyError`
- C) `ValueError`
- D) `NameError`

**4. Which exception does `open("missing.txt")` raise if the file doesn't exist?**
- A) `FileNotFoundError`
- B) `IndexError`
- C) `ZeroDivisionError`
- D) `OSError` is never raised

**5. When does the `else` block of a `try` run?**
- A) Always
- B) Only when an exception happened
- C) Only when nothing inside `try` failed
- D) Never; `else` isn't allowed with `try`

**6. When does `finally` run?**
- A) Only when there was an error
- B) Only when there was no error
- C) Every time, error or not
- D) Only at the end of the program

**7. Why use `with open(...) as f:`?**
- A) It makes the file read faster
- B) It closes the file automatically, even if an error happens
- C) It creates a backup of the file
- D) It's required to read binary files

**8. Which reads a file one line at a time?**
- A) `f.read()`
- B) `for line in f:`
- C) `f.write()`
- D) `open("notes.txt", "x")`

**9. What does mode `"w"` do?**
- A) Reads the file
- B) Adds to the end of the file
- C) Creates the file, or wipes it if it already exists
- D) Fails if the file exists

**10. Which mode adds text to the end of an existing file?**
- A) `"r"`
- B) `"w"`
- C) `"a"`
- D) `"x"`

**11. What does mode `"x"` do?**
- A) Deletes the file
- B) Creates a new file and fails if it already exists
- C) Opens the file read-only
- D) Opens the file in binary mode

**12. Does `f.write("hello")` add a new line at the end?**
- A) Yes, always
- B) No, you have to add `\n` yourself
- C) Only in mode `"a"`
- D) Only on Windows

**13. How do you create your own exception?**
- A) `def MyError(): ...`
- B) `class MyError(Exception): ...`
- C) `exception MyError: ...`
- D) `import MyError`

---

### Part B – What's the output?

**14.** The user types `0`. What is printed?
```python
try:
    age = int(input("Age: "))
    per_year = 1000 / age
except ValueError:
    print("Please type a whole number.")
except ZeroDivisionError:
    print("Age can't be zero.")
else:
    print(f"{per_year:.1f} per year")
finally:
    print("Thanks!")
```

**15.** What is in `list.txt` after this runs?
```python
with open("list.txt", "w") as f:
    f.write("milk\n")
with open("list.txt", "a") as f:
    f.write("eggs\n")
with open("list.txt", "w") as f:
    f.write("bread\n")
```

---

### Part C – Fix the bug

**16.** This crashes the first time it runs, because `notes.txt` doesn't exist yet. Make it print `No notes yet.` instead.
```python
with open("notes.txt") as f:
    print(f.read())
```

**17.** Every new note overwrites the old ones. Fix it so notes are added to the end.
```python
note = input("Note: ")
with open("my_notes.txt", "w") as f:
    f.write(note + "\n")
```

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Explanation | Video |
|---|--------|-------------|-------|
| 1 | B | Exceptions happen at runtime; syntax errors are found before. | 0:18 |
| 2 | B | Uncaught exceptions stop the program with a traceback. | 0:41 |
| 3 | C | Right type (str), but a value that can't become an int. | 1:43 |
| 4 | A | The file isn't there. | 1:43 |
| 5 | C | `else` runs only when nothing failed. | 2:26 |
| 6 | C | `finally` always runs, which makes it good for clean-up. | 2:26 |
| 7 | B | `with` closes the file for you. | 7:01 |
| 8 | B | Looping over the file gives one line at a time. | 7:13 |
| 9 | C | `"w"` creates or wipes the file. | 9:12 |
| 10 | C | `"a"` appends to the end. | 9:15 |
| 11 | B | `"x"` creates a new file and refuses to overwrite. | 9:20 |
| 12 | B | `write()` adds no new line, so add `\n`. | 10:22 |
| 13 | B | A custom exception is a class that inherits from `Exception`. | 1:54 |
| 14 | `Age can't be zero.` then `Thanks!` | `1000 / 0` raises `ZeroDivisionError`; `finally` still runs. | 2:55 |
| 15 | `bread` | The last `"w"` wipes the file before writing. | 9:12 |
| 16 | Wrap it in `try:` … `except FileNotFoundError: print("No notes yet.")` | Catch the error you expect. | 16:31 |
| 17 | Change `"w"` to `"a"`. | Append mode keeps the old notes. | 9:15 |

</details>

---

If this module helped you, you can support the channel:

- **Buy me a coffee** at [buymeacoffee.com/the_growthclub](https://buymeacoffee.com/the_growthclub) ☕
- **Subscribe** to [The Growth Club](https://www.youtube.com/@TheGrowthClubOfficial) on YouTube
- **Star** this repo so others can find it

Every coffee helps me keep making free Python lessons. Thank you! 🙏
