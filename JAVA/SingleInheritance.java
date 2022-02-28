class A{
	int a,b;
	void getdata(int x,int y) {
		a=x;
		b=y;
	}
	int add() {
		System.out.println("Method of Super class");
		return a+b;
	}
}

class B extends A{
	int mul() {
		System.out.println("Method of Sub class");
		return a*b;
	}
}
public class SingleInheritance {
	public static void main(String arg[]) {
		B obj=new B();
		obj.getdata(5, 8);
		int add,mul;
		add=obj.add();
		System.out.println("Addition is "+add);
		mul=obj.mul();
		System.out.println("Multiplication is "+mul);
	}

}
