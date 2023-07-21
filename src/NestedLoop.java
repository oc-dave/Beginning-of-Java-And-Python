public class NestedLoop {
    public static void main(String[] args) {
        for (int a = 0; a < 10; a++) {

            for (int b = 0; b <= a; b++) {
                System.out.print("# ");
            }
            for (int c = 0; c < 10 - a; c++) {
                System.out.print("  ");
            }
            for (int d = 0; d < 10 - a; d++) {
                System.out.print("# ");
            }
            for (int b = 0; b <= a; b++) {
                System.out.print("  ");
            }
            for (int b = 0; b <= a; b++) {
                System.out.print("  ");
            }
            for (int b = 0; b < 10 - a; b++) {
                System.out.print("# ");
            }
            for (int b = 0; b < 10 - a; b++) {
                System.out.print("  ");
            }
            for (int b = 0; b <= a; b++) {
                System.out.print("# ");
            }
            System.out.println();
        }
    }
}
