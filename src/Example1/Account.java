package Example1;
    import java.util.Scanner;

    public class Account {
        private String pin;
        private double balance;
        private String name;
        private boolean isLocked;

        public Account() {
            pin = null;
            balance = 0;
            name = null;
            isLocked = false;
        }

        public void setPin() {
            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.print("Set a 4-digit PIN for your account: ");
                pin = scanner.nextLine();
                if (pin.matches("\\d{4}")) {
                    System.out.println("PIN set successfully.");
                    break;
                } else {
                    System.out.println("PIN must be a 4-digit number.");
                }
            }
        }

        public boolean getName() {
            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.print("Enter your name: ");
                name = scanner.nextLine();
                if (!name.matches(".*\\d.*")) {
                    System.out.println("Welcome, " + name + "!");
                    break;
                } else {
                    System.out.println("Please enter a valid name without digits.");
                }
            }
            return true;
        }

        public void deposit(double amount) {
            try {
                if (amount > 0) {
                    balance += amount;
                    System.out.printf("Deposit of $%.2f successful.%n", amount);
                    displayBalance();
                } else {
                    System.out.println("Invalid deposit amount. Amount must be greater than zero.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid numeric amount.");
            }
        }

        public boolean checkPin(String enteredPin) {
            return pin.equals(enteredPin);
        }

        public boolean withdraw(double amount) {
            if (amount > 0 && amount <= balance) {
                balance -= amount;
                System.out.printf("Withdrawal of $%.2f successful.%n", amount);
                displayBalance();
            } else {
                System.out.println("Invalid withdrawal amount or insufficient funds.");
            }
            return true;
        }

        public double checkBalance() {
            return balance;
        }

        public void displayBalance() {
            System.out.printf("Current balance: $%.2f%n", balance);
        }

        public void lock() {
            isLocked = true;
        }

        public void unlock() {
            isLocked = false;
        }

    }
