interface C1{
	int roll=101;
	void dispa();
}

interface C2{
	dispb();
}

class C3 implements C1,C2{
	public void dispa() {
		System.out.println("Roll number is "+roll);
	}
	public void dispb() {
		System.out.println("Method from B interface");
	}
}

public class UsingInterface {
	public static void main(String arg[]) {
		C3 obj=new C3();
		obj.dispa();
		obj.dispb();
	}

}
