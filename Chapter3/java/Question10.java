import java.util.Scanner;
public class Question10 {
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);


System.out.println("Enter the principal amount: ");
double principal = input.nextDouble();

System.out.println("Enter annual interest rate in decimal: ");
double interestRate = input.nextDouble();

for (int years =1; years <= 30; years++){
	double amount = principal *Math.pow(1 + interestRate, years);
	System.out.printf("the amount at the end of year %d, is %.2f\n", years, amount);
		}
	}
}