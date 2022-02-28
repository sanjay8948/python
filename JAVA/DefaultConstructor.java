class Test{
	int a,b;
	Test() {
		System.out.println("This is default constructor.");
		a=10;
		b=20;
	}
	void disp() {
		System.out.println("Value of A is "+a);
		System.out.println("Value of B is "+b);
	}
}
public class DefaultConstructor {
	public static void main(String args[]) {
		Test obj=new Test();
		obj.disp();
	}

}
