public class Question6 {
public static void main(String[] args) {

int square = 0;
int cube = 0;

System.out.printf("%8s %8s %8s\n", "Number", "Square", "Cube");


for (int number = 0; number <=5; number++){
    square = number * number;
    cube = number * number * number;
    System.out.printf("%8d %8d %8d \n",  number, square, cube);}
	}
}


    
