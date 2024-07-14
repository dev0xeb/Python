import java.util.Scanner;
public class MorgageCalculator {
	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);

System.out.println("Enter the amount the client wishes to borrow: ");
int principal = input.nextInt();

System.out.println("Enter the yearly interest offered by the mortgage: ");
double annualInterestRate = input.nextInt();

System.out.println("Enter the duration of the loan in years: ");
int duration = input.nextInt();

double monthlyInterestRate =  (annualInterestRate/100) / 12;
System.out.printf("the monthly interest rate is %.4f", monthlyInterestRate);

int loanTerminMonths = duration * 12;
System.out.println("The loan term in months " + loanTerminMonths);

double clientMonthlyPayment = principal * (monthlyInterestRate *Math.pow(1 + monthlyInterestRate, loanTerminMonths)) / (Math.pow( 1 + monthlyInterestRate, loanTerminMonths) -1);
System.out.printf("The client monthly payment is %.2f ", clientMonthlyPayment);
	}
}

