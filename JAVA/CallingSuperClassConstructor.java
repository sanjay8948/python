class Ay{
	int a;
	Ay(){
		System.out.println("Constructor in class Ay");
	}
}

class By extends Ay{
	By(){
		System.out.println("Constructor in class By");
	}
}
public class CallingSuperClassConstructor {
	public static void main(String arg[]) {
		By obj=new By();
	}

}
