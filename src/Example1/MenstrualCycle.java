package Example1;

import java.time.LocalDate;

public class MenstrualCycle {
    private final LocalDate startDate;
    private final int safePeriod;
    private final int cycleLength;
    private final int menstrualPeriod;

    public MenstrualCycle(LocalDate startDate, int cycleLength, int menstrualPeriod) {
        this.startDate = startDate;
        this.cycleLength = cycleLength;
        this.menstrualPeriod = menstrualPeriod;
        this.safePeriod = cycleLength - menstrualPeriod;
    }

    public int getCycleLength() {
        return cycleLength;
    }
    public LocalDate calculateNextPeriod() {
        return startDate.plusDays(cycleLength);
    }

    public LocalDate calculateFertileWindow() {
        return startDate.plusDays(cycleLength - safePeriod);
    }

    public LocalDate calculateOvulationDate() {
        return startDate.plusDays(cycleLength - safePeriod + menstrualPeriod);
    }

}
