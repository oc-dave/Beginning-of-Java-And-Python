import random
from dave_package.Account import Account


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = random.randint(3000000000, 9000000000)
        account = Account()
        account.set_pin()
        account.get_name()
        self.accounts[account_number] = account
        print(f"Account created successfully! Your account number is: {account_number}")
        return account_number

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if account := self.get_account(account_number):
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account := self.get_account(account_number):
            account.withdraw(amount)

    def transfer(self, from_account_number, to_account_number, pin, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            from_account = self.accounts[from_account_number]
            if from_account.check_pin(pin):
                to_account = self.accounts[to_account_number]

                if from_account.withdraw(amount):
                    to_account.deposit(amount)
                    print(
                        f"Transfer of ${amount:.2f} from account {from_account_number} to account {to_account_number} successful.")
            else:
                print("Incorrect PIN for the source account.")
        else:
            print("One or both accounts not found.")

    def check_account_balance(self, account_number):
        if account := self.get_account(account_number):
            balance = account.check_balance()
            print(f"Account Number: {account_number}, balance: ${balance:.2f}")
        else:
            print("Account not found.")

    def check_account_details(self, account_number):
        if account := self.get_account(account_number):
            print(f"Account Number: {account_number}")
            print(f"Account Holder: {account.get_name()}")
            print(f"Account Balance: ${account.check_balance():.2f}")
        else:
            print("Account not found.")

    def lock_account(self, account_number):
        if account := self.get_account(account_number):
            account.lock()
            print(f"Account {account_number} locked successfully.")
        else:
            print("Account not found.")

    def unlock_account(self, account_number):
        if account := self.get_account(account_number):
            account.unlock()
            print(f"Account {account_number} unlocked successfully.")
        else:
            print("Account not found")

    def add_account_number(self, to_account_number):
        if to_account_number not in self.accounts:
            self.accounts[to_account_number] = Account()
            print(f"Account {to_account_number} added successfully.")
        else:
            print("Account already exists.")
