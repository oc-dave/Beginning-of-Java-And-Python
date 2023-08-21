package Example1;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

public class Bank {
    private final Map<Long, Account> accounts;

    public Bank() {
        accounts = new HashMap<>();
    }

    public long createAccount() {
        Random random = new Random();
        long accountNumber = 3000000000L + (long) (random.nextDouble() * (6000000000L));
        Account account = new Account();
        account.setPin();
        account.getName();
        accounts.put(accountNumber, account);
        System.out.println("Account created successfully! Your account number is: " + accountNumber);
        return accountNumber;
    }

    public Account getAccount(long accountNumber) {
        if (accounts.containsKey(accountNumber)) {
            return accounts.get(accountNumber);
        } else {
            System.out.println("Account not found.");
            return null;
        }
    }

    public void deposit(long accountNumber, double amount) {
        Account account = getAccount(accountNumber);
        if (account != null) {
            account.deposit(amount);
        } else {
            System.out.println("Account not found.");
        }
    }

    public void withdraw(long accountNumber, double amount) {
        Account account = getAccount(accountNumber);
        if (account != null) {
            account.withdraw(amount);
        }
    }

    public void transfer(long fromAccountNumber, long toAccountNumber, String pin, double amount) {
        Account fromAccount = getAccount(fromAccountNumber);
        Account toAccount = getAccount(toAccountNumber);

        if (fromAccount != null && toAccount != null) {
            if (fromAccount.checkPin(pin)) {
                if (fromAccount.withdraw(amount)) {
                    toAccount.deposit(amount);
                    System.out.printf("Transfer of $%.2f from account %d to account %d successful.%n",
                            amount, fromAccountNumber, toAccountNumber);
                } else {
                    System.out.println("Insufficient funds.");
                }
            } else {
                System.out.println("Incorrect PIN for the source account.");
            }
        } else {
            System.out.println("One or both accounts not found.");
        }
    }

    public void checkAccountBalance(long accountNumber) {
        Account account = getAccount(accountNumber);
        if (account != null) {
            System.out.printf("Account Number: %d, Balance: $%.2f%n", accountNumber, account.checkBalance());
        }
    }

    public void checkAccountDetails(long accountNumber) {
        Account account = getAccount(accountNumber);
        if (account != null) {
            System.out.println(account.getName());
            System.out.println("Account Number: " + accountNumber);
            System.out.printf("Account Balance: $%.2f%n", account.checkBalance());
        }
    }

    public void lockAccount(long accountNumber) {
        Account account = getAccount(accountNumber);
        if (account != null) {
            account.lock();
            System.out.println("Account " + accountNumber + " locked successfully.");
        }
    }

    public void unlockAccount(long accountNumber) {
        Account account = getAccount(accountNumber);
        if (account != null) {
            account.unlock();
            System.out.println("Account " + accountNumber + " unlocked successfully.");
        }
    }

    public void addAccountNumber(long toAccountNumber) {
        if (!accounts.containsKey(toAccountNumber)) {
            accounts.put(toAccountNumber, new Account());
            System.out.println("Account " + toAccountNumber + " added successfully.");
        } else {
            System.out.println("Account already exists.");
        }
    }
}
