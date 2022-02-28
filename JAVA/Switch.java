import java.util.Scanner;
class Switch {
    public static void main(String arg[])
    {
    	Scanner obj=new Scanner(System.in);
    	int roll;
    	System.out.println("Enter roll number ");
    	roll=obj.nextInt();
    	
    	switch(roll)
    	{
    	case 101:
    		System.out.println("Student name : Ramesh");
    		break;
    	case 102:
    		System.out.println("Student name : Mukesh");
    		break;
    	case 103:
    		System.out.println("Student name : Shyam");
    		break;
    	default :
    		System.out.println("Not found");
    	}
    }
}
