import java.util.Scanner;
class ConditionalOperator {
public static void main(String arg[])
    {
	Scanner obj=new Scanner(System.in);
	int a,b,c;
	System.out.println("Enter two number");
	a=obj.nextInt();
	b=obj.nextInt();
	
	c=(a>b)?a:b;
	System.out.println("Greater value is "+c);
    }
}
