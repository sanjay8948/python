class Calculation{
	int a,b;
	void Calc(int x){
		a=x;
		System.out.println("Square is "+(a*a));
	}
	void Calc(int x,int y) {
		a=x;
		b=y;
		System.out.println("Sum is "+(a+b));
	}
}

public class MethodOverloading {
	public static void main(String arg[]) {
		Calculation obj=new Calculation();
		obj.Calc(6);
		obj.Calc(5,9);
	}

}
