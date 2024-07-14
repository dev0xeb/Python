import java.util.Scanner;
public class Question8 {
	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);

int total = 0;
int product = 0;
double average =0;
int[] numbers = new int[3];


for (int count=1; count <=3; count++){
	System.out.print("Enter a number");
	int userInput = input.nextInt();
	System.out.print("you entered " + userInput);
	number[] = userInput;
	total += userInput;
	product *= userInput;
	average = total /3;}

System.out.println("the total of the numbers" + total);
System.out.println("the product of the numbers" + product);
System.out.println("the average of the numbers" + average);

int smallestNumber = Integer.MIN_VALUE;

int largestNumber = Integer.MAX_VALUE;

System.out.println("The smallest number is " + smallestNumber);
System.out.println("The largest number is " + largestNumber);
}
}

