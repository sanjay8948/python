import pack_1.*;
public class PackSub extends PackBase {
	int n=200;
	void dispsub() {
		System.out.println("Class Sub");
		System.out.println("Val ="+val);
		System.out.println("n ="+n);
	}

}

class PackMain{
	public static void main(String arg[]) {
		PackSub obj=new PackSub();
		obj.disp();
		obj.dispsub();
	}
}
