# Python Foundations – Module 3 Knowledge Check
**Lists & Loops**

Try to answer without rewatching. The answer key with video timestamps is at the bottom.

---

### Part A – Multiple choice

**1. How do you create a list in Python?**
- A) `(12, 40, 7)`
- B) `{12, 40, 7}`
- C) `[12, 40, 7]`
- D) `<12, 40, 7>`

**2. What is the index of the first item in a list?**
- A) `0`
- B) `1`
- C) `-1`
- D) It depends on the list

**3. `expenses = [12.5, 40.0, 7.25]`. What is `expenses[-1]`?**
- A) `12.5`
- B) `40.0`
- C) `7.25`
- D) An error

**4. Which function gives the number of items in a list?**
- A) `count()`
- B) `size()`
- C) `length()`
- D) `len()`

**5. What does `append()` do?**
- A) Adds an item to the start of the list
- B) Adds an item to the end of the list
- C) Removes the last item
- D) Sorts the list

**6. What does `expenses.remove(40.0)` remove?**
- A) The item at index 40
- B) Every item equal to `40.0`
- C) The first item equal to `40.0`
- D) The last item

**7. In `for amount in expenses:`, what is `amount`?**
- A) The number of items
- B) Each item of the list, one at a time
- C) The index of each item
- D) The whole list

**8. Which numbers does `range(5)` produce?**
- A) 1, 2, 3, 4, 5
- B) 0, 1, 2, 3, 4, 5
- C) 0, 1, 2, 3, 4
- D) 1, 2, 3, 4

**9. Which `range()` gives 1, 2, …, 12 (the months of a year)?**
- A) `range(12)`
- B) `range(1, 12)`
- C) `range(1, 13)`
- D) `range(0, 13)`

**10. What does the third number in `range(0, 10, 2)` mean?**
- A) Repeat twice
- B) Jump by 2 each time
- C) Stop at 2
- D) Start at 2

**11. What does `break` do inside a loop?**
- A) Skips to the next pass
- B) Stops the loop straight away
- C) Restarts the loop
- D) Pauses the program

**12. A variable that starts at 0 and has a value added on every pass of a loop is called…**
- A) an index
- B) an accumulator (a running total)
- C) a range
- D) a constant

---

### Part B – What's the output?

**13.** What is printed?
```python
expenses = [12.50, 40.00, 7.25]
expenses.append(20)
expenses.remove(40.00)
print(expenses)
```

**14.** What does each line print?
```python
print(list(range(1, 6)))
print(list(range(0, 10, 2)))
print(list(range(5, 0, -1)))
```

**15.** What is printed?
```python
total = 0
for amount in [10, 20, 30]:
    total += amount
print(total)
```

**16.** What is printed?
```python
names = ["Vishal", "Raj", "Li"]
for i in range(len(names)):
    print(i, names[i])
```

---

### Part C – Your turn

**17. Grade book (the module exercise).** Use `range()` to ask for 5 test scores and store them in a list. Print the average (1 decimal), the highest and the lowest score, and count how many scores are 50 or more. Bonus: let the user choose how many scores to enter.

Submit your solution as a PR to [github.com/CodeMitVishal/python-foundations](https://github.com/CodeMitVishal/python-foundations) – I'll review it!

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Explanation | Video |
|---|--------|-------------|-------|
| 1 | C | Square brackets make a list. | 0:35 |
| 2 | A | Counting starts at 0, not 1. | 0:54 |
| 3 | C | `-1` is the last item. | 1:16 |
| 4 | D | `len()` counts the items. | 4:27 |
| 5 | B | `append()` adds to the end. | 4:36 |
| 6 | C | `remove()` deletes only the first match. | 4:36 |
| 7 | B | The loop variable holds each item in turn. | 5:00 |
| 8 | C | `range(stop)` starts at 0 and never includes `stop`. | 11:31 |
| 9 | C | The stop value is not included, so use 13. | 19:32 |
| 10 | B | The third number is the step. | 19:08 |
| 11 | B | `break` ends the loop early, like when the loan is paid off. | 23:25 |
| 12 | B | Start at 0, add on every pass: a running total. | 6:34 |
| 13 | `[12.5, 7.25, 20]` | `append` adds 20 at the end, `remove` takes out 40.0. | 4:36 |
| 14 | `[1, 2, 3, 4, 5]`, `[0, 2, 4, 6, 8]`, `[5, 4, 3, 2, 1]` | start/stop/step; a negative step counts down. | 19:08 |
| 15 | `60` | 0 + 10 + 20 + 30. | 6:34 |
| 16 | `0 Vishal`, `1 Raj`, `2 Li` | `range(len(names))` gives the positions 0, 1, 2. | 19:45 |

</details>

---

## ☕ Enjoyed this quiz?

[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-support%20us-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/codemitvishal)

### Bonus – while loops, slicing, tuples and sets

**B1.** What does `days[::-1]` give for `days = ["Mon", "Tue", "Wed"]`?

**B2.** When do you use `while` instead of `for`?

**B3.** What's the difference between `break` and `continue`?

**B4.** `len(set(["a", "b", "a"]))` = ?

<details><summary><b>Bonus answers</b></summary>

B1: `["Wed", "Tue", "Mon"]` · B2: when you don't know in advance how many times (repeat until a condition changes) · B3: `break` leaves the loop; `continue` skips to the next round · B4: `2`. Revisit `05_while_break_continue.py` and `06_slicing_tuples_sets.py`.

</details>

If this module helped you, you can support the channel:

- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it

Every coffee helps me keep making free Python lessons. Thank you! 🙏
