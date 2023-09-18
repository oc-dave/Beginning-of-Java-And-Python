from dave_package.Bank import Bank


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Bank!")
        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money")
        print("5. Check account balance")
        print("6. Lock account")
        print("7. Exit")

        choice = input("Please enter your choice (1-7): ")

        if choice == "1":
            account_number = input("Enter your account number: ")
            bank.create_account(account_number)

        elif choice == "2":
            account_number = input("Enter your account number: ")
            amount = float(input("Enter the amount to deposit: "))
            bank.deposit(account_number, amount)

        elif choice == "3":
            account_number = input("Enter your account number: ")
            amount = float(input("Enter the amount to withdraw: "))
            bank.withdraw(account_number, amount)

        elif choice == "4":
            from_account_number = input("Enter your account number: ")
            to_account_number = input("Enter the recipient's account number: ")
            amount = float(input("Enter the amount to transfer: "))
            pin = input("Enter your PIN: ")
            bank.transfer(from_account_number, to_account_number, amount, pin)

        elif choice == "5":
            account_number = input("Enter your account number: ")
            bank.check_balance(account_number)

        elif choice == "6":
            account_number = input("Enter your account number: ")
            bank.lock_account(account_number)

        elif choice == "7":
            print("Thank you for using the Bank. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()