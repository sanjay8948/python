import java.util.Scanner;
class Addition{
	int a,b;
	void get_value() {
		Scanner obj=new Scanner(System.in); 
		System.out.println("Enter two numbers ");
		a=obj.nextInt();
		b=obj.nextInt();
	}
	void Add() {
		System.out.println("Addition is : "+(a+b));
	}
}
public class CreateClass1{
	public static void main(String args[]) {
		Addition obj1=new Addition();
		obj1.get_value();
		obj1.Add();
	}

}

