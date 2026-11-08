"""Module 7 · Debugging: find and fix bugs like a pro

1. READ THE TRACEBACK from the BOTTOM up: the last line says WHAT went wrong,
   the lines above say WHERE (file and line number).
2. Check your assumptions with print() (quick) or breakpoint() (powerful).
3. Use the VS Code debugger: click left of a line number to set a red dot
   (a breakpoint), press F5, then step through the code and watch the variables.

Run it:  python 07_files_exceptions/06_debugging.py
"""
import sys
import traceback


# --- 1. A buggy function -------------------------------------------------------------------
def average_price(prices):
    total = 0
    for p in prices:
        total += p
    return total / len(prices)


# --- 2. Reading a traceback ------------------------------------------------------------------
try:
    average_price([])                       # an empty list...
except ZeroDivisionError:
    print("----- traceback (read it from the bottom up) -----")
    traceback.print_exc(limit=2, file=sys.stdout)
print("""
How to read it:
  ZeroDivisionError: division by zero           <- WHAT happened (last line)
  File "...06_debugging.py", line 20, in average_price   <- WHERE
      return total / len(prices)                <- the exact line
So: len(prices) was 0. Fix: handle the empty list.
""")

# --- 3. The 6 errors you'll meet most --------------------------------------------------------------
examples = {
    "NameError":      "print(pirce)          -> a typo, or the variable isn't defined yet",
    "TypeError":      '"Age: " + 30          -> mixing types: use f"Age: {30}" or str(30)',
    "ValueError":     'int("abc")            -> right type, impossible value',
    "IndexError":     "[1, 2, 3][5]          -> the list is shorter than you think",
    "KeyError":       'person["email"]       -> that key doesn\'t exist: use .get()',
    "IndentationError": "a missing or extra space at the start of a line",
}
for name, meaning in examples.items():
    print(f"  {name:<17} {meaning}")

# --- 4. print() debugging: show the values, with labels ------------------------------------------------
def total_with_tax(prices, tax):
    subtotal = sum(prices)
    print(f"DEBUG {subtotal=} {tax=}")      # the = shows the name AND the value
    return subtotal * tax                    # bug! should be subtotal * (1 + tax)

print("\nresult:", total_with_tax([10, 20], 0.19), "<- far too small: the DEBUG line shows why")

# --- 5. breakpoint(): pause INSIDE your program ------------------------------------------------------------
# Remove the # below and run the file. The program stops there and you can type:
#   p subtotal      print a variable         n   run the next line
#   s               step into a function     c   continue to the end
#   l               show where you are       q   quit
#
# def fixed_total(prices, tax):
#     subtotal = sum(prices)
#     breakpoint()
#     return subtotal * (1 + tax)
#
# In VS Code it's even easier: set a red-dot breakpoint and press F5.
# Hover over any variable to see its value.

# --- 6. Rubber duck debugging ---------------------------------------------------------------------------
# Explain your code, line by line, out loud (to a rubber duck, or a friend).
# Half the time you find the bug while explaining. Seriously.
