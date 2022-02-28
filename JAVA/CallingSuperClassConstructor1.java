class Cx{
	int a;
	Cx(int x){
		a=x;
		System.out.println("Value of A "+a);
	}
}

class Cy extends Cx{
	int b;
	Cy(int x,int y){
		super(x);
		b=y;
		System.out.println("Value of B "+b);
	}
}
public class CallingSuperClassConstructor1 {
	public static void main(String arg[]) {
		Cy obj=new Cy(100,200);
	}

}
