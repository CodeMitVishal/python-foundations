# Python Foundations – Module 1 Knowledge Check
**Data Types, Variables, Input & Arithmetic**

Try to answer without rewatching. The answer key with video timestamps is at the bottom.

---

### Part A – Multiple choice

**1. What is the data type of `42` in Python?**
- A) `float`
- B) `int`
- C) `str`
- D) `bool`

**2. What is the data type of `4.99`?**
- A) `int`
- B) `decimal`
- C) `float`
- D) `double`

**3. What does `type("10")` return?**
- A) `<class 'int'>`
- B) `<class 'float'>`
- C) `<class 'str'>`
- D) `<class 'number'>`

**4. Which values can a `bool` hold?**
- A) `0` to `9`
- B) `True` or `False`
- C) `"yes"` or `"no"`
- D) Any text

**5. Python is a *dynamically typed* language. What does that mean?**
- A) You must declare the type of every variable before using it
- B) Python works out the type from the value at runtime
- C) A variable's type can never change
- D) Python only supports numbers

**6. Which variable name is NOT valid?**
- A) `tax_rate`
- B) `length1`
- C) `1length`
- D) `birth_year`

**7. Which naming style does Python recommend for variables?**
- A) `TaxRate`
- B) `taxRate`
- C) `tax_rate`
- D) `TAX-RATE`

**8. Why does `4.99 * 10` print `49.900000000000006`?**
- A) It's a bug in Python
- B) Floats are approximate values
- C) `10` is a string
- D) Multiplication always adds extra digits

**9. Which command shows the installed Python version?**
- A) `python --version`
- B) `python -check`
- C) `version python`
- D) `pip version`

**10. What does `round(4.7992, 2)` return?**
- A) `4.7`
- B) `4.8`
- C) `4.80`
- D) `5`

**11. What does `input()` always return?**
- A) An `int`
- B) A `float`
- C) A `str`
- D) Whatever type the user typed

**12. Which operator gives the remainder of a division?**
- A) `/`
- B) `//`
- C) `%`
- D) `**`

---

### Part B – What's the output?

**13.** Fill in each result:
```python
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(7 ** 2)
```

**14.** The user types `30`. What is printed?
```python
age = input("How old are you? ")
age = int(age)
print(f"Next year you will be {age + 1}")
```

**15.** What is printed?
```python
name = "Vishal"
print(name.upper(), len(name))
```

**16.** What happens here if the user types `30`, and why?
```python
age = input("How old are you? ")
print(age + 1)
```

**17.** The user enters `2026` as the current year and `1996` as the birth year. What are `age`, `months` and `days`?
```python
current = int(input("Current year: "))
birth_year = int(input("Birth year: "))
age = current - birth_year
months = age * 12
days = age * 365
```

---

### Part C – Your turn

**18. Tip calculator (the module exercise).** Ask for the bill amount, the tip percentage and how many people are paying. Print the tip, the total and each person's share, all rounded to 2 decimals.

Submit your solution as a PR to [github.com/VishalCodingNinja/python-foundations](https://github.com/VishalCodingNinja/python-foundations) – I'll review it!

---

<details>
<summary><b>Answer key (click to open)</b></summary>

| # | Answer | Explanation | Video |
|---|--------|-------------|-------|
| 1 | B | Whole numbers are `int`. | 1:35 |
| 2 | C | Decimals are `float`. | 1:51 |
| 3 | C | Anything in quotes is a string, even `"10"`. | 3:17 |
| 4 | B | `bool` is either `True` or `False`. | 2:16 |
| 5 | B | Python assigns the type from the value at runtime. | 2:43 |
| 6 | C | Names cannot start with a digit. | 3:39 |
| 7 | C | `lowercase_with_underscores` (snake_case). | 3:39 |
| 8 | B | Floats are approximate, hence the trailing digits. | 3:56 |
| 9 | A | `python --version` | 4:52 |
| 10 | B | Rounds to 2 decimals; trailing zeros aren't shown. | 7:09 |
| 11 | C | Input from the console is always a string; convert it with `int()`. | 13:13 |
| 12 | C | `%` is the remainder (modulo) operator. | 8:02 |
| 13 | `3.5`, `3`, `1`, `49` | `/` divides, `//` floor-divides, `%` gives the remainder, `**` is power. | 8:15 |
| 14 | `Next year you will be 31` | `int()` converts the text `"30"` to the number 30. | 13:56 |
| 15 | `VISHAL 6` | `.upper()` makes it uppercase; `len()` counts 6 characters. | 18:31 |
| 16 | `TypeError` | `age` is still the string `"30"`, and you can't add a number to a string. Convert it with `int(age)` first. | 13:13 |
| 17 | `30`, `360`, `10950` | 2026 − 1996 = 30; 30 × 12 = 360; 30 × 365 = 10,950. | 21:03 |

</details>

---

## ☕ Enjoyed this quiz?

[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-support%20us-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/the_growthclub)

If this module helped you, you can support the channel:

- **Buy me a coffee** at [buymeacoffee.com/the_growthclub](https://buymeacoffee.com/the_growthclub) ☕
- **Subscribe** to [The Growth Club](https://www.youtube.com/@TheGrowthClubOfficial) on YouTube
- **Star** this repo so others can find it

Every coffee helps me keep making free Python lessons. Thank you! 🙏
