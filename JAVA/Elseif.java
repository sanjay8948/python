import java.util.Scanner;
class Elseif {
    public static void main(String arg[])
    {
    	Scanner obj=new Scanner(System.in);
    	int marks;
    	char grade;
    	System.out.println("Enter your marks ");
    	marks=obj.nextInt();
    	
    	if (marks>=85)
    	{
    		grade='A';
    	}
    	else if(marks>=75)
    	{
    		grade='B';
    	}
    	else if(marks>=60)
    	{
    		grade='C';
    	}
    	else
    	{
    		grade='D';
    	}
    	System.out.println("Grade "+grade);
    }
}
