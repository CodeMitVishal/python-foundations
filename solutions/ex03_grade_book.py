"""Solution · Exercise 3: grade book (Module 3)

Task: exercises/ex03_grade_book.py
Run it:  python solutions/ex03_grade_book.py

How it works:
  1. Collect: a for loop over range(1, 6) runs 5 times. Each pass asks for
     one score, turns the text into a float and appends it to the list.
  2. Summarise: built-in functions work on the whole list at once:
     sum() adds everything, len() counts the items, max()/min() pick the
     largest and smallest. Average = sum / count.
  3. Count passes: a second loop visits each score. A counter starts at 0
     and goes up by 1 whenever a score is 50 or more (accumulator pattern).

Walk-through with the sample scores 72, 45, 88, 50, 63:
  scores  -> [72.0, 45.0, 88.0, 50.0, 63.0]
  average -> 318 / 5 = 63.6
  passed  -> 72 yes, 45 no, 88 yes, 50 yes (>= includes 50), 63 yes = 4

What you practise: lists, append(), for loops, range(), sum/len/max/min,
an if inside a loop, and f-string formatting.
"""

# Start with an empty list and add one score per pass of the loop
scores = []
for i in range(1, 6):  # i is 1, 2, 3, 4, 5, used to number the prompts
    score = float(input(f"Score {i}: "))
    scores.append(score)

# The average is the sum of the scores divided by how many there are
average = sum(scores) / len(scores)

# Accumulator pattern: start a counter at 0 and add 1 for every pass
passed = 0
for score in scores:
    if score >= 50:
        passed += 1

print(f"Average: {average:.1f}")  # :.1f shows 1 decimal place
print("Highest:", max(scores))
print("Lowest:", min(scores))
print(f"Passed: {passed} of {len(scores)}")
