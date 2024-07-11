import java.util.Scanner;
public class BankApp {
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

	int count = 0;
	int userInput = 0;
	int totalDeposit = 0;
	int balance =0;
	int withdraw = 0;
	
	while (userInput != -1){
	System.out.println("1. Deposit \n 2. Withdraw \n 3. Balance \n -1. Exit");

	System.out.println("Enter a number: ");
	userInput = input.nextInt();

	if (userInput == 1){
		System.out.println("Enter DEPOSIT amount: ");
		int deposit = input.nextInt();
		totalDeposit += deposit;}
	
	else if (userInput == 2){
		System.out.println("Enter WITHDRAWAL amount: ");
		withdraw = input.nextInt();
		if (withdraw > totalDeposit || withdraw < 0)
			System.out.println("Invalid amount input");
		else
			System.out.println("Withdrawal successfull");}
	
	else if (userInput == 3){
       	balance = totalDeposit - withdraw;
        System.out.println(balance);}

	else
		break;
		}
	
		
	
	}
}

	
