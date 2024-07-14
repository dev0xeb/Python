import java.util.Scanner;
public class Question12 {
	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);


System.out.println("Enter a five digit number: ");
int userInput = input.nextInt();
{
	if (userInput < 10000 || userInput > 99999);
	System.out.println("Enter a five digit number: ");
	userInput = input.nextInt();
}
int firstNum = userInput / 10000;
int secondNum = (userInput / 1000) % 10;
int thirdNum = (userInput / 100) % 10;
int fourthNum = (userInput / 10) % 10;
int fifthNum = userInput % 10;

if (firstNum  == fifthNum && secondNum == fourthNum)
	System.out.println("Number is a palindrome");
else
	System.out.println("Number is not palindrome");
	}
}