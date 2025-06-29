class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        #self.account_balance = amount + self.account_balance
        self.account_balance += amount
#        if amount > 0:
#           self.account_balance += amount
#      else:
#         print("You cannot deposit a negative amount or Zero amount")

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True
    def display_balance(self):
        print(f"Your Current account balance is {self.account_balance}")


