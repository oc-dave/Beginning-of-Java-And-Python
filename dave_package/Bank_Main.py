from dave_package.Bank import Bank


def main():  # sourcery skip: low-code-quality
    bank = Bank()
    account_number = None

    while True:
        print("\nWelcome to yahoo boy Bank!")

        if account_number is not None:
            print(f"Current Account Number: {account_number}")

        print("1. Create an account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money")
        print("5. Check account balance")
        print("6. Check account details")
        print("7. Lock account")
        print("8. Unlock account ")
        print("9. Exit")

        choice = input("Please enter your choice (1-8): ")

        if choice == "1" and account_number is None:
            account_number = bank.create_account()

        elif choice == "2":
            if account_number:
                amount = float(input("Enter the amount to deposit: "))
                bank.deposit(account_number, amount)
            else:
                print("Account not found. Please create an account first.")

        elif choice == "3" and account_number:
            amount = float(input("Enter the amount to withdraw: "))
            bank.withdraw(account_number, amount)

        elif choice == "4":
            if account_number:
                to_account_number = input("Enter the 10-digit account number to transfer to: ")
                if to_account_number.isdigit() and len(to_account_number) == 10:
                    pin = input("Enter your PIN: ")

                    amount = int(input("Enter the amount to transfer: "))
                    if to_account_number not in bank.accounts:
                        bank.add_account_number(to_account_number)
                        bank.transfer(account_number, to_account_number, pin, amount)
                        print("Account transfer successful")
                else:
                    print("Invalid account number. Account number must be 10 digits.")
            else:
                print("Account not found. Please create an account first.")

        elif choice == "5":
            if account_number:
                bank.check_account_balance(account_number)
            else:
                print("Account not found. Please create an account first.")

        elif choice == "6":
            if account_number:
                bank.check_account_details(account_number)
            else:
                print("Account not found. Please create an account first.")

        elif choice == "7":
            if account_number:
                bank.lock_account(account_number)
            else:
                print("Account not found. Please create an account first.")

        elif choice == "8":
            if account_number:
                bank.unlock_account(account_number)
            else:
                print("Account not found. Please create an account first.")

        elif choice == "9":
            print("Thanks for using my bank.....Goodbye.")
            break


if __name__ == "__main__":
    main()
