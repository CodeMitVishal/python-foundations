"""Exercise 6: Bank accounts  (Module 6: classes and inheritance)

Write a class BankAccount with:
  __init__(self, owner, balance=0)
  deposit(self, amount)      adds to the balance
  withdraw(self, amount)     refuses (prints "Declined...") if the
                             balance is too low, otherwise subtracts
  describe(self)             returns e.g. "Vishal: 150.00"

Then write SavingsAccount(BankAccount) that also takes a rate
(default 0.02) and has add_interest(self), which adds balance * rate.

Try it:
    vishal = BankAccount("Vishal", 100)
    vishal.deposit(50)
    vishal.withdraw(500)       # Declined: Vishal has only 150.00
    raj = SavingsAccount("Raj", 1000, rate=0.05)
    raj.add_interest()
    for account in [vishal, raj]:
        print(account.describe())

Expected output:
    Declined: Vishal has only 150.00
    Vishal: 150.00
    Raj: 1050.00

Hint: call super().__init__(owner, balance) inside SavingsAccount.
Solution: solutions/ex06_bank_account.py
"""

# TODO 1: write the BankAccount class

# TODO 2: write SavingsAccount, inheriting from BankAccount

# TODO 3: paste the "Try it" lines above and run the file
