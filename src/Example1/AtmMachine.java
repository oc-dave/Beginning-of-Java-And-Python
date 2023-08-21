package Example1;

import java.util.Scanner;

public class AtmMachine {
    private static final Scanner input = new Scanner(System.in);
    public static void main(String[] args) {

        String mainMenu = """
                Welcome to Dave's Bank
                Press
                1-> To Open Account
                2-> To Deposit
                3-> To Withdraw
                4-> Transfer
                5-> To Check Balance
                6-> To Exit
                """;
        String userInput = input(mainMenu);
        switch (userInput.charAt(0)) {
            case '1'-> openAccount();
            case '2'-> deposit();
            case '3'-> withdraw();
            case '4'-> transfer();
            case '5'-> checkBalance();
            case '6'-> exit();
            default-> displayMainMenu();
        }
    }

    private static void displayMainMenu() {
    }

    private static void checkBalance() {
    }

    private static void transfer() {
    }

    private static void exit() {
    }

    private static void withdraw() {
        
    }

    private static void deposit() {
        
    }

    private static void openAccount() {
        
    }

    private static String input(String mainMenu) {
        return input.nextLine();
    }
}
