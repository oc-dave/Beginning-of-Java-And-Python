class BankAccount:
    def __init__(self):
        self.pin = 1234
        self.accounts = {}

    def register(self, account_number: int):
        if account_number not in self.accounts:
            self.accounts.update({account_number: 0})
            print("Account registered")
        else:
            print("Account already registered")

            return self.pin

    def get_pin(self):
        return self.pin

    def incorrect_pin(self, account_number, account_pin):
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        elif self.accounts[account_number] != account_pin:
            raise ValueError("Invalid PIN")
        else:
            print("Correct PIN")

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        else:
            print("Deposit successful")
        self.accounts[account_number] += amount
        return self.accounts[account_number]

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found")

        balance = self.accounts[account_number]
        print("Balance:", balance)

        return balance

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient funds")
        else:
            print("Account not found")

    def transfer_with_pin(self, account_number1, account_number2, amount, pin):
        if account_number1 not in self.accounts:
            raise KeyError(f"Account number {account_number1} does not exist")
        elif account_number2 not in self.accounts:
            raise KeyError(f"Account number {account_number2} does not exist")
        elif self.accounts[account_number1] != pin:
            raise ValueError("Incorrect PIN")
        elif self.accounts[account_number1] < amount:
            raise ValueError("Insufficient funds")
        else:
            self.accounts[account_number1] -= amount
            self.accounts[account_number2] += amount
            print("Transfer successful")

    def find_account(self, account_number):
        return account_number in self.accounts

    def lock_account(self, account_number):
        if account_number in self.accounts:
            self.accounts[account_number] = 0
        return 0
    print('Account locked')
