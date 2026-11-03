# Python Foundations – Module 2 Knowledge Check
**Conditionals, Operators & Imports**

Try to answer without rewatching. The answer key with video timestamps is at the bottom.

---

### Part A – Multiple choice

**1. Which keyword checks another condition when the first `if` is false?**
- A) `else if`
- B) `elif`
- C) `elseif`
- D) `then`

**2. When does the `else` block run?**
- A) Always
- B) Only when the `if` condition is true
- C) Only when none of the conditions above it are true
- D) Never, it's optional

**3. What does `5 != 3` return?**
- A) `True`
- B) `False`
- C) `2`
- D) An error

**4. What does `2 >= 4` return?**
- A) `True`
- B) `False`
- C) `4`
- D) `None`

**5. `age > 18 and has_id` is `True` only when…**
- A) either side is true
- B) both sides are true
- C) neither side is true
- D) `age` is exactly 18

**6. What does `not True` return?**
- A) `True`
- B) `False`
- C) `None`
- D) `0`

**7. What is the difference between `=` and `==`?**
- A) There is no difference
- B) `=` compares values, `==` assigns
- C) `=` assigns a value, `==` compares values
- D) `==` is only for strings

**8. In Rock, Paper, Scissors, which choice beats paper?**
- A) Rock
- B) Paper
- C) Scissors
- D) Nothing beats paper

**9. What does `import random` do?**
- A) Creates a random file
- B) Makes the ready-made `random` module available in your program
- C) Downloads a package from the internet
- D) Picks a random line of your code

**10. What does `math.sqrt(81)` print?**
- A) `9`
- B) `9.0`
- C) `81`
- D) `40.5`

**11. Which line picks a random item from the list `options`?**
- A) `random.pick(options)`
- B) `random.choice(options)`
- C) `options.random()`
- D) `random(options)`

**12. Where should `import` lines usually go?**
- A) At the bottom of the file
- B) Inside every function
- C) At the top of the file
- D) Anywhere, after you use the module

---

### Part B – What's the output?

**13.** What is printed when `temp = 14`?
```python
if temp >= 30:
    print("Hot – drink water")
elif temp >= 15:
    print("Nice weather")
else:
    print("Bring a jacket")
```

**14.** What does each line print?
```python
print(5 == 5)
print(9 > 4)
print(True or False)
print(not (5 == 5))
```

**15.** What range of numbers can this print?
```python
import random
print(random.randint(1, 6))
```

**16.** What is printed?
```python
from datetime import date
print(type(date.today().year))
```

---

### Part C – Your turn

**17. Guess the Number (the module exercise).** The computer picks a secret number between 1 and 10 with `random`. Ask the user for a guess, then tell them if they won or what the number was. Bonus: handle input outside the range, like `-4` or `15`.

Submit your solution as a PR to [github.com/VishalCodingNinja/python-foundations](https://github.com/VishalCodingNinja/python-foundations) – I'll review it!

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Explanation | Video |
|---|--------|-------------|-------|
| 1 | B | `elif` means "else if". | 0:44 |
| 2 | C | `else` catches everything the conditions above didn't. | 1:21 |
| 3 | A | 5 is not equal to 3, so `!=` is `True`. | 3:34 |
| 4 | B | 2 is not greater than or equal to 4. | 4:30 |
| 5 | B | `and` needs both sides to be true. | 4:45 |
| 6 | B | `not` flips the value. | 5:15 |
| 7 | C | One `=` assigns; `==` compares. | 5:41 |
| 8 | C | Scissors cut paper. | 7:22 |
| 9 | B | A module is ready-made code that ships with Python. | 8:05 |
| 10 | B | `sqrt` always returns a float. | 9:16 |
| 11 | B | `random.choice()` picks one item from a sequence. | 11:22 |
| 12 | C | Import once at the top, then use it anywhere below. | 10:06 |
| 13 | `Bring a jacket` | 14 fails both `>= 30` and `>= 15`, so `else` runs. | 2:43 |
| 14 | `True`, `True`, `True`, `False` | `or` needs only one side true; `not` flips `True` to `False`. | 3:21 |
| 15 | 1 to 6 | `randint` includes both ends. | 13:23 |
| 16 | `<class 'int'>` | The year is a whole number. | 9:22 |

</details>

---

## ☕ Enjoyed this quiz?

[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-support%20us-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/the_growthclub)

If this module helped you, you can support the channel:

- **Buy me a coffee** at [buymeacoffee.com/the_growthclub](https://buymeacoffee.com/the_growthclub) ☕
- **Subscribe** to [The Growth Club](https://www.youtube.com/@TheGrowthClubOfficial) on YouTube
- **Star** this repo so others can find it

Every coffee helps me keep making free Python lessons. Thank you! 🙏
