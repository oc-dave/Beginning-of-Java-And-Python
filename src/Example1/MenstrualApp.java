package Example1;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.Scanner;

class MenstrualApp{
    public MenstrualApp(LocalDate startDate, int cycleLength, int menstrualPeriod) {
        this.menstrualCycle = new MenstrualCycle(startDate, cycleLength, menstrualPeriod);
    }

    private final MenstrualCycle menstrualCycle;
    public LocalDate calculateNextPeriod() {
    return menstrualCycle.calculateNextPeriod();
    }

    public LocalDate calculateFertileWindow() {
    return menstrualCycle.calculateFertileWindow();
    }

    public LocalDate calculateOvulationDate() {
    return menstrualCycle.calculateOvulationDate();
    }

    public void sendNotification(LocalDate date) {
        LocalTime currentTime = LocalTime.now();
        String greeting;

        if (currentTime.isBefore(LocalTime.NOON)) {
            greeting = "Good morning,";
        } else if (currentTime.isBefore(LocalTime.of(17, 0))) {
            greeting = "Good afternoon,";
        } else {
            greeting = "Good evening,";
        }

        Scanner input = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String user = input.nextLine();
        System.out.println(greeting + user + "!, " + "sent on " + date);

    }

}
