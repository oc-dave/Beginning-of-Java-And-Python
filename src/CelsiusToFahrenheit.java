import java.util.GregorianCalendar;
import java.util.Scanner;

public class CelsiusToFahrenheit {

        public static void main(String [] args) {
            Scanner input = new Scanner(System.in);

            System.out.print("Enter temperature in celsius : ");
            double celsius = input.nextDouble();

            double fahrenheit = (celsius * 9 / 5) + 32;

            System.out.printf("%.2f Celsius is %.2f Fahrenheit ",celsius, fahrenheit  );


        }

}
