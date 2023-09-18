class Account:
    def __init__(self):
        self.pin = None
        self.balance = 0
        self.name = None

    def set_pin(self):
        self.pin = input("Enter a 4-digit PIN: ")
        while not self.pin.isdigit() or len(self.pin) != 4:
            print("PIN must be a 4-digit number.")
            self.pin = input("Enter a 4-digit PIN: ")
        print("PIN set successfully")

    def get_name(self):
        self.name = input("Enter your name: ")
        while self.name == "" or self.name.isdigit():
            print("Please enter a valid name.")
            self.name = input("Enter your name: ")
        print(self.name)

    def check_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount:.2f} successful. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of ${amount:.2f} successful. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance
