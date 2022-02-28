abstract class X{
	abstract void disp();
	void display() {
		System.out.println("Method from X class");
	}
}

class Y extends X{
	void disp() {
		System.out.println("Method defined in Y class");
	}
}

public class AbstractClass {
	public static void main(String arg[]) {
		Y obj=new Y();
		obj.disp();
		obj.display();
	}

}
