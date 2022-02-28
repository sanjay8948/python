import java.util.Scanner;
public class Exception1 {
	public static void main(String arg[]) {
		Scanner obj=new Scanner(System.in);
		System.out.println("Enter the value of a,b and c : ");
		int a=obj.nextInt();
		int b=obj.nextInt();
		int c=obj.nextInt();
		
/*		try {
			int x=int a/(b-c);
			System.out.println("X = "+x);
		}
		catch(Exception e) {
			System.out.println("value of b and c can not be equal");
		}  
 */		
		try {
			int x=a/(b-c);
			System.out.println("X = "+x);
		}
		catch(ArithmeticException e) {
			System.out.println("Division by zero");
		}          
		
		int y=a/(b+c);
		System.out.println("Y = "+y);
	}

}
