import java.util.Scanner;
public class Question5 {
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);

	System.out.println("Enter first number: ");
	int num1 = input.nextInt();

	System.out.println("Enter second number: ");
	int num2 = input.nextInt();

if (num1 == num2)
    System.out.println(num1 + "is equal to " + num2);
else
    System.out.println(num1 + "is not equals to " + num2);

if (num1 > num2)
    System.out.println(num1 + "is greater than " + num2);
else
    System.out.println(num1 + "is not greater than " + num2);

if (num1 <= num2)
    System.out.println(num1 + "is lesser than or equal to " + num2);
else
    System.out.println(num1 + "is greater than or equals to " + num2);

	}
}

