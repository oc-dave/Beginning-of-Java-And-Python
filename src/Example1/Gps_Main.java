package Example1;

import java.util.Scanner;

import static Example1.GPS.getGPSState;

public class Gps_Main {
    public static class GPS_MAIN {
        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter your state: ");
            String state = scanner.nextLine();

            GPS gps = getGPSState(state);
            if (gps != null) {
                System.out.println("Geopolitical zone: " + gps.name());
            } else {
                System.out.println("Invalid State entered!");
            }

        }
    }
}

