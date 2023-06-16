import java.util.Scanner;

public class NumberComparison {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter an integer: ");
        int number = scanner.nextInt();
        
        int square = (number * number);
        
        if (number + square > 100) {
            System.out.println("The number and its square are greater than 100.");
        } else 
        
        if (number + square == 100) {
            System.out.println("The number and its square are equal to 100.");
        } else 
        
        if (number + square != 100) {
            System.out.println("The number and its square are not equal to 100.");
        } else 
        
        if (number + square < 100) {
            System.out.println("The number and its square are less than 100.");
        } else
        
        scanner.close();
    }
}

