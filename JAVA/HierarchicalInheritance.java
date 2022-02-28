class One{
	int x=10,y=20;
	void disp() {
		System.out.println("Method of class One");
		System.out.println("Value of X is "+x);
		System.out.println("Value of Y is "+y);
	}
}

class Two extends One{
	void add() {
		System.out.println("Method of class Two");
		System.out.println("Addition is "+(x+y));
	}
}

class Three extends One{
	void mul() {
		System.out.println("Method of class Three");
		System.out.println("Multiplication is "+(x*y));
	}
}
public class HierarchicalInheritance {
	public static void main(String args[]) {
		Two obj1=new Two();
		Three obj2=new Three();
		obj1.disp();
		obj1.add();
		obj2.mul();
	}

}
