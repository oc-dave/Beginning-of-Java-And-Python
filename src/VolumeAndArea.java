import java.util.Scanner;

public class VolumeAndArea {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the radius : ");
        double radius = input.nextDouble();

        System.out.print("Enter the length :  ");
        double length = input.nextDouble();

        double area = radius * radius * 3.14;

        double volume = area * length;

        System.out.printf("The area is %.1f ",area);
        System.out.printf("The volume is %.1f ",volume);



    }
}
