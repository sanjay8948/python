import java.util.Scanner;
class Square {
    public static void main(String args[])
    {
    	int no;
    	Scanner obj=new Scanner(System.in);
    	System.out.println("Enter a number ");
    	no=obj.nextInt();
    	System.out.println("Square of number is "+(no*no));
    }
}
