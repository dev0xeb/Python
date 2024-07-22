public class DivideorSquare {
	public static double divideorsquare(int number) {
	
	if (number % 5 == 0)
	return Math.pow(number, 0.5);	

	else
	return number % 5;
}

	public static void main(String[] args){
	int number = 10;
	double result = divideorsquare(number);
	System.out.print(result);
	}
}