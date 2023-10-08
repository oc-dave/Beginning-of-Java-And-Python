class Account:
    def __init__(self):
        self.pin = None
        self.balance = 0
        self.name = None
        self.is_locked = False

    def set_pin(self):
        while True:
            self.pin = input("Set a 4-digit PIN for your account: ")
            if self.pin.isdigit() and len(self.pin) == 4:
                print("PIN set successfully.")
                break
            else:
                print("PIN must be a 4-digit number.")

    def get_name(self):
        while True:
            try:
                self.name = input("Enter your name: ")
                if not self.name.isdigit():
                    print(f"Welcome, {self.name}!")
                    break
                else:
                    print("Please enter a valid name without digits.")
            except (ValueError, SyntaxError, TypeError):
                print("PLease enter a Valid name")

    def deposit(self, amount):
        try:
            amount = int(amount)
            if amount > 0:
                self.balance += amount
                print(f"Deposit of ${amount:.2f} successful.")
                self.display_balance()
            else:
                print("Invalid deposit amount. Amount must be greater than zero.")
        except (ValueError, SyntaxError, TypeError):
            print("Please enter a valid numeric amount.")

    def check_pin(self, pin):
        return self.pin == pin

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount:.2f} successful.")
            self.display_balance()
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def check_balance(self):
        return self.balance

    def display_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def lock(self):
        self.is_locked = True

    def unlock(self):
        self.is_locked = False

    def is_account_locked(self):
        return self.is_locked


