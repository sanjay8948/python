import java.util.Scanner;
class Nestedif {
    public static void main(String arg[])
    {
    	Scanner obj=new Scanner(System.in);
    	int a,b,c,great;
    	System.out.println("Enter three number ");
    	a=obj.nextInt();
    	b=obj.nextInt();
    	c=obj.nextInt();
    	
    	if(a>b)
    	{
    		if(a>c)
    		{
    			great=a;
    		}
    		else
    		{
    			great=c;
    		}
       }
    	else
    	{
    		if(b>c)
    		{
    			great=b;
    		}
    		else
    		{
    			great=c;
    		}
    	}
    	System.out.println("Greater value is "+great);
    }
}
