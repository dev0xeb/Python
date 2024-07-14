import java.util.Scanner;
public class Question11 {
	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);

double totalMiles = 0;
double totalGallons = 0;
double totalMilesGallon = 0;
double countTrips = 0;
double gallonsUsed;

System.out.println("Enter the gallons used or -1 to end: ");
gallonsUsed = input.nextDouble();

while (gallonsUsed != -1){

System.out.println("Enter the number of miles driven: ");
double milesDriven = input.nextDouble();

double milesPerGallon = milesDriven / gallonsUsed;
System.out.println("the miles/gallon for this tank was" + milesPerGallon);

totalGallons += gallonsUsed;
totalMiles += milesDriven;
countTrips +=1;
totalMilesGallon += milesPerGallon;

System.out.println("Enter the gallons used or -1 to end: ");
gallonsUsed = input.nextDouble();
}

System.out.println("total gallons used is " + totalGallons);
System.out.println("total miles driven is " + totalMiles);

double averageMilesGallon = totalMilesGallon /countTrips;
System.out.println("the overall average miles/gallon was " + averageMilesGallon);
	}
}