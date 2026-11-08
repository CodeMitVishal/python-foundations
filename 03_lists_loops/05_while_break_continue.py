"""Module 3 · while loops, break and continue

A `for` loop runs once per item. A `while` loop runs AS LONG AS a condition is
True, which is perfect when you don't know in advance how many times:
"keep asking until the answer is valid", "keep playing until the user quits".

Run it:  python 03_lists_loops/05_while_break_continue.py
"""

# --- 1. A basic while loop: count down ------------------------------------------------
count = 3
while count > 0:            # checked BEFORE every round
    print("countdown:", count)
    count -= 1              # without this line the loop would never end!
print("lift off!")

# --- 2. Saving up: we don't know how many months it takes -------------------------------
savings, months = 0, 0
while savings < 1000:
    savings += 150
    months += 1
print(f"1000 EUR saved after {months} months (you have {savings} EUR)")

# --- 3. break: leave the loop immediately ------------------------------------------------
answers = ["abc", "-5", "42", "7"]          # pretend these were typed by a user
for text in answers:
    if text.isdigit():
        print("first valid number:", text)
        break                               # stop: we found what we wanted
    print("not a number, skipping:", text)

# --- 4. continue: skip the REST of this round, go to the next one ---------------------------
for n in range(1, 8):
    if n % 2 == 0:
        continue                            # skip even numbers
    print("odd:", n)

# --- 5. The classic input loop (the pattern you'll use most) ---------------------------------
# while True:
#     answer = input("Type a number (or q to quit): ")
#     if answer == "q":
#         break                       # the ONLY way out of `while True`
#     if not answer.isdigit():
#         print("Please type digits only.")
#         continue
#     print(int(answer) * 2)
fake_inputs = iter(["x", "5", "q"])           # simulates typing so this demo runs by itself
while True:
    answer = next(fake_inputs)
    if answer == "q":
        print("bye!")
        break
    if not answer.isdigit():
        print(f"{answer!r} is not a number")
        continue
    print(f"{answer} x 2 = {int(answer) * 2}")

# Stuck in an endless loop? Press Ctrl + C in the terminal to stop it.
