package Example1;


import static sun.security.util.KeyUtil.validate;

public class Time {

    private int hour;

    private int minute;

    private int second;

    public Time(int hour, int minute, int second){
        validate(hour, minute, second);

        this.hour = hour;
        this.minute = minute;
        this.second = second;

    }


    public int getHour(){
        return hour;
    }

    public int getMinute(){
        return minute;
    }

    public int getSecond(){
        return second;
    }

    public Time(){

    }

    private static void validate(int hour, int minute, int second) {
        if (hour < 0 || hour > 23) {
            throw new IllegalArgumentException("Invalid hour");
        }
        if (minute < 0 || minute > 59) {
            throw new IllegalArgumentException("Invalid minute");
        }
        if (second < 0 || second > 59) {
            throw new IllegalArgumentException("Invalid second");
        }
    }


}
