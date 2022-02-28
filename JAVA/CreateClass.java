class Addition{
	int a,b;
	void get_value(int x,int y) {
		a=x;
		b=y;
	}
	void Add() {
		System.out.println("Addition is : "+(a+b));
	}
}
public class CreateClass {
	public static void main(String args[]) {
		Addition obj=new Addition();
		obj.get_value(5, 9);
		obj.Add();
	}

}
