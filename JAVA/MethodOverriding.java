class Super{
	int x=10;
	void disp() {
		System.out.println("Super "+x);
	}
}

class Sub extends Super{
	int y=20;
	void disp() {
		System.out.println("Super "+x);
		System.out.println("Sub "+y);
	}
}
public class MethodOverriding {
	public static void main(String arg[]) {
		Sub obj=new Sub();
		obj.disp();
	}

}
