package Example1;

import java.util.Scanner;

public class DiaryTest {
        public static void main(String[] args) {
            System.out.println("Welcome to your Diary App");
            System.out.println("Please enter your name");
            Scanner scanner = new Scanner(System.in);
            String name = scanner.nextLine();
            System.out.println("Hello " + name);

            System.out.println("Please enter your age");
            int age = scanner.nextInt();
            scanner.nextLine();  // Consume newline
            System.out.println("Your age is " + age);

            System.out.println("Please enter your gender");
            String gender = scanner.nextLine();
            System.out.println("Your gender is " + gender);

            System.out.println("""
                    1.Create a Diary Account
                    2.Add Entry
                    
                
                    """);
        }
    }

