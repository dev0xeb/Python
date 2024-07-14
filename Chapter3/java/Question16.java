import java.util.Scanner;

public class GreatestNumberFinder {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = 0; 
        
for (int count = 0; count < 10; count++) {
System.out.print("Enter number " + (count + 1) + ": ");
int user_input = scanner.nextInt(); // Read user input
            
System.out.println("You entered: " + user_input); 
if (user_input > number) {
number = user_input; 
            }
        }
System.out.println("The greatest number is: " + number);
        
       
    }
}
