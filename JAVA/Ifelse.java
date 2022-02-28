import java.util.Scanner;
class Ifelse {
    public static void main(String args[])
    {
    	Scanner obj=new Scanner(System.in);
    	System.out.println("Enter your salary");
    	int sal=obj.nextInt();
    	
    	if(sal>=10000)
    	{
    		int b=(sal*10)/100;
    		sal=sal+b;
    	}
    	else
    	{
    		int b=(sal*5)/100;
    		sal=sal+b;
    	}
    	System.out.println("Your salary is "+sal);
    }
}
