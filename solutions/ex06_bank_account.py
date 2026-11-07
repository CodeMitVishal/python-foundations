"""Solution · Exercise 6: bank accounts (Module 6)

Task: exercises/ex06_bank_account.py
Run it:  python solutions/ex06_bank_account.py
"""


class BankAccount:
    # balance=0 is a default, so a new account can start empty
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    # Refuse the withdrawal instead of letting the balance go below zero.
    # Returning True or False tells the caller whether it worked.
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Declined: {self.owner} has only {self.balance:.2f}")
            return False
        self.balance -= amount
        return True

    def describe(self):
        return f"{self.owner}: {self.balance:.2f}"


# A SavingsAccount is a BankAccount that also earns interest
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.02):
        # Let BankAccount set owner and balance, then add the new attribute
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.balance += self.balance * self.rate


vishal = BankAccount("Vishal", 100)
vishal.deposit(50)         # the balance is now 150
vishal.withdraw(500)       # Declined: Vishal has only 150.00
raj = SavingsAccount("Raj", 1000, rate=0.05)
raj.add_interest()         # 1000 plus 5% is 1050
# describe() works on both, because SavingsAccount inherits it
for account in [vishal, raj]:
    print(account.describe())
