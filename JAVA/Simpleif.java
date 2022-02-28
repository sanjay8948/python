import java.util.Scanner;
class Simpleif {
    public static void main(String args[])
    {
    	Scanner obj=new Scanner(System.in);
    	int sal,b;
    	System.out.print("Enter your salary : ");
    	sal=obj.nextInt();
    	if (sal>10000)
    	{
    		b=(sal*10)/100;
    		sal=sal+b;
    	}
    	System.out.print("Your salary is : "+sal);
    }
    
}
