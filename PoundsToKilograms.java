import java.util.Scanner;
	public class PoundsToKilograms{
	
		public static void main(String args[]){
		Scanner scan = new Scanner(System.in);
		
		System.out.print("Enter weight in pounds :");
		
		double weight = scan.nextDouble();
		
		double kilogram = (weight * 0.454);
		
		System.out.printf("Pounds to kilogram %.4f%n", kilogram);
		
		
		
	}
	
	
	
	
}
		
