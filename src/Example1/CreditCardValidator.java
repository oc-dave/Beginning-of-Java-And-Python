package Example1;
import java.util.Scanner;

public class CreditCardValidator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a credit card number: ");
        String cardNumber = input.next();

        int sum = 0;
        boolean odd = false;

        for (int i = cardNumber.length() - 1; i >= 0; i--) {
            int digit = Integer.parseInt(String.valueOf(cardNumber.charAt(i)));
            if (odd == !odd) digit *= 2;
            if (digit > 9) digit -= 9;
            sum += digit;
        }

        if (sum % 10 == 0) {
            System.out.println("Valid credit card");
        } else {
            System.out.println("Invalid credit card");
        }
    }
}
