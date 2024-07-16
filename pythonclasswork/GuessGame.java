import java.util.Scanner;
import java.util.Random;
public class GuessGame {

	public static void main(String[] args) {
	Scanner input = new Scanner(System.in);
	Random rand = new Random();

System.out.println("Welcome to clinton's guess game");

int guessNumber = rand.nextInt(1000);
int counter = 0;
int userInput = 0;
int decision = 0;


while (userInput != guessNumber) {
System.out.println("Enter a numnber between 1 and 1000: ");
userInput = input.nextInt();
counter++;

if (userInput > guessNumber)
System.out.println("Too high, try again");
else if(userInput < guessNumber)
System.out.println("Too low, try again");
else if (userInput ==  guessNumber)
System.out.println("Congratulations, you guessed the number");}
        if (counter <= 10)
           System.out.println("you attempted " + counter + " times before winning you are a CHAMP");
        else
            System.out.println("you attempted " + counter + " times before winning, you need to up your game");

	
}
}

