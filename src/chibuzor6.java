public class chibuzor6 {
    public static void main(String[] args) {
        int x = 4;
        int sum = 0;
        do {
            System.out.print(x + " ");
            sum += x;
            x = x * 4;
        }

        while (x < 2000);
        System.out.print("= "+ sum);
    }

}
