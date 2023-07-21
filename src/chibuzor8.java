public class chibuzor8 {
    public static void main(String[] args) {
        int x = 4;
        int sum1 = 0;
        do {
            System.out.print(x + " ");
            sum1 += x;
            x = x * 4;
        }

        while (x < 2000);
        System.out.print("= "+ sum1 + " , ");

        int y = 8;
        int sum2 = 0;
        do {
            System.out.print(y + " ");
            sum2 += y;
            y = y * 8;
        }
        while (y < 40000);
        System.out.print("= " + sum2);


    }
}
