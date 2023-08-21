package Example1;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Bank bank = new Bank();
        long accountNumber = 0;

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\nWelcome to Yahoo Boy Bank!");

            if (accountNumber != 0) {
                System.out.println("Current Account Number: " + accountNumber);
            }

            System.out.println("1. Create an account");
            System.out.println("2. Deposit money");
            System.out.println("3. Withdraw money");
            System.out.println("4. Transfer money");
            System.out.println("5. Check account balance");
            System.out.println("6. Check account details");
            System.out.println("7. Lock account");
            System.out.println("8. Unlock account");
            System.out.println("9. Exit");

            System.out.print("Please enter your choice (1-9): ");
            int choice = scanner.nextInt();
            scanner.nextLine();  // Consume newline

            switch (choice) {
                case 1 -> {
                    if (accountNumber == 0) {
                        accountNumber = bank.createAccount();
                    } else {
                        System.out.println("Account already exists.");
                    }
                }
                case 2 -> {
                    if (accountNumber != 0) {
                        System.out.print("Enter the amount to deposit: $");
                        double amount = scanner.nextDouble();
                        bank.deposit(accountNumber, amount);
                    } else {
                        System.out.println("Account not found. Please create an account first.");
                    }
                }
                case 3 -> {
                    if (accountNumber != 0) {
                        System.out.print("Enter the amount to withdraw: $");
                        double amount = scanner.nextDouble();
                        bank.withdraw(accountNumber, amount);
                    } else {
                        System.out.println("Account not found. Please create an account first.");
                    }
                }
                case 4 -> {
                    if (accountNumber != 0) {
                        System.out.print("Enter the 10-digit account number to transfer to: ");
                        long toAccountNumber = scanner.nextLong();
                        scanner.nextLine();  // Consume newline
                        System.out.print("Enter your PIN: ");
                        String pin = scanner.nextLine();
                        System.out.print("Enter the amount to transfer: $");
                        double transferAmount = scanner.nextDouble();
                        bank.addAccountNumber(toAccountNumber);
                        bank.transfer(accountNumber, toAccountNumber, pin, transferAmount);
                    } else {
                        System.out.println("Account not found. Please create an account first.");
                    }
                }
                case 5 -> {
                    if (accountNumber != 0) {
                        bank.checkAccountBalance(accountNumber);
                    } else {
                        System.out.println("Account not found. Please create an account first.");
                    }
                }
                case 6 -> {
                    if (accountNumber != 0) {
                        bank.checkAccountDetails(accountNumber);
                    } else {
                        System.out.println("Account not found. Please create an account first.");
                    }
                }
                case 7 -> {
                    if (accountNumber != 0) {
                        bank.lockAccount(accountNumber);
                    } else {
                        System.out.println("Account not found. Please create an account first.");
                    }
                }
                case 8 -> {
                    if (accountNumber != 0) {
                        bank.unlockAccount(accountNumber);
                    } else {
                        System.out.println("Account not found. Please create an account first.");
                    }
                }
                case 9 -> {
                    System.out.println("Thanks for using Yahoo Boy Bank. Goodbye.");
                    scanner.close();
                    System.exit(0);
                }
                default -> System.out.println("Invalid choice. Please enter a valid option.");
            }
        }
    }
}
