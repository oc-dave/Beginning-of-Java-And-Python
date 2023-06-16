import java.util.Scanner;
	public class Acceleration {
	
		public static void main(String args[]){
		Scanner deck = new Scanner(System.in);
		
		System.out.println("Enter starting velocity: ");
		double startingVelocity = deck.nextDouble();
		
		System.out.println("Enter ending velocity: ");
		double endingVelocity = deck.nextDouble();
		
		System.out.println("Enter time in seconds: ");
		double timeInSeconds = deck.nextDouble();
		
		double acceleration = (endingVelocity - startingVelocity) / timeInSeconds;
		
		System.out.printf("The average acceleration is %.4f%n",acceleration);
		
		
		
		
		
	}
	
	
	
	
}
		
