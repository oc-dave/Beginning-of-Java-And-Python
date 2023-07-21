public class chibuzor7 {
    public static void main(String[] args) {
        int y = 8;
        int sum = 0;
        do {
            System.out.print(y + " ");
            sum += y;
            y = y * 8;
        }
        while (y < 40000);
        System.out.print("= " + sum);
    }
}
