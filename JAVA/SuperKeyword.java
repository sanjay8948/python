class Ax{
	int no;
	void message() {
		System.out.println("Number in super class "+no);
	}
}

class Bx extends Ax{
	int no;
	Bx(int a,int b){
		super.no=a;
		no=b;
	}
	void message() {
		System.out.println("Number in subclass "+no);
	}
	void disp() {
		super.message();
		message();
	}
}
public class SuperKeyword {
	public static void main(String arg[]) {
		Bx obj=new Bx(5,8);
		obj.disp();
	}

}
