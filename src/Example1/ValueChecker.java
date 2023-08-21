package Example1;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ValueChecker {

    public static boolean containsSpecialCharacter(String str) {
        Pattern pattern = Pattern.compile("[^a-zA-Z0-9 ]");
        Matcher matcher = pattern.matcher(str);
        return matcher.find();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter String value: ");
        String input = scanner.nextLine();
        if (containsSpecialCharacter(input)) {
            System.out.println("The string contains a special character.");
        } else {
            System.out.println("The string does not contain a special character.");
        }
    }
}
