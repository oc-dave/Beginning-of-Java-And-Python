from dave_package.Account import Account


class Bank:
    def __init__(self):
        self.name = None
        self.accounts = {}

    def create_account(self, account_number):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account()
            self.accounts[account_number].set_pin()
            self.accounts[account_number].get_name()
            print(f"{self.name}Your Account is created successfully")
        else:
            print("Account already exists")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        print("Account not found")
        return None

    def deposit(self, account_number, amount):
        if account := self.get_account(account_number):
            account.deposit(amount)

    def withdraw(self, account_number, amount):
        if account := self.get_account(account_number):
            account.withdraw(amount)

    def transfer(self, from_account_number, to_account_number, amount, pin):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if from_account and to_account:
            if from_account.check_pin(pin):
                if from_account.check_balance() >= amount:
                    from_account.withdraw(amount)
                    to_account.deposit(amount)
                    print("Transfer successful")
                else:
                    print("Insufficient funds")
            else:
                print("Incorrect PIN")

    def check_balance(self, account_number):
        if account := self.get_account(account_number):
            balance = account.check_balance()
            print(f"Your account balance is: ${balance:.2f}")

    def lock_account(self, account_number):
        if account := self.get_account(account_number):
            account.set_pin()  # Resetting the PIN effectively locks the account
            print("Account locked")
