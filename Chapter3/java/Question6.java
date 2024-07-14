import java.util.Scanner;
public class Question6 {
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

	System.out.println("What is your problem: ");
	String num1 = input.nextLine();

	System.out.println("Have you had this problem before: Enter 1 for Yes and 0 for No");
	int num2 = input.nextInt();

if (num2 == 1)
System.out.print("Well, you have it again");

else if (num2 == 0)
System.out.print("Well, you have it now");

else
System.out.print("Invalid input, try again");
	}
}
