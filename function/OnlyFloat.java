public class OnlyFloat {
	public static int onlyfloats(double num1, double num2){

	if (num1 % 1 == 0 && num2 % 1 == 0)
	return 2;

	else if (num1 % 1 != 0 && num2 % 1 != 0)
	return 0;

	else
	return 1;
}


	public static void main(String[] args){
	double num1 = 12.1;
	double num2 = 23;
	int result = onlyfloats(num1, num2);
	System.out.print(result);
	}
}
