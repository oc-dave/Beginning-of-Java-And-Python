package Example1;

import java.time.LocalDate;
import java.util.Scanner;

public class MenstrualAppTest {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        LocalDate startDate = LocalDate.now();
        System.out.print("Enter the cycle length: ");
        int cycleLength = input.nextInt();

        System.out.print("Enter the menstrual period: ");
        int menstrualPeriod = input.nextInt();

        MenstrualApp menstrualApp = new MenstrualApp(startDate, cycleLength, menstrualPeriod);

        menstrualApp.sendNotification(LocalDate.now());

        System.out.println("Your next period is: " + menstrualApp.calculateNextPeriod());
        System.out.println("Your fertile window is on: " + menstrualApp.calculateFertileWindow());
        System.out.println("Your ovulation date is on: " + menstrualApp.calculateOvulationDate());
    }
}



