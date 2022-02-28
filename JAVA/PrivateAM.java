class AM1{
	private int data=40;
	private void msg() {
		System.out.println("Hello world");
	}
}

public class PrivateAM {
	public static void main(String args[]) {
		AM1 obj=new AM1();
		System.out.println(obj.data);    //compile time error
		obj.msg();    //compile time error
	}

}
