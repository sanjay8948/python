//please run this at cmd
public class Exception2 {
	public static void main(String arg[]) {
		int a,b,ans;
		try {
			a=Integer.parseInt(arg[0]);
			b=Integer.parseInt(arg[1]);
			try {
				ans=a/b;
				System.out.println("Result = "+ans);
			}
			catch(ArithmeticException e) {
				System.out.println("Division by zero");
			}
		}
		catch(NumberFormatException e) {
			System.out.println("Incorrect argument type");
		}
	}

}
