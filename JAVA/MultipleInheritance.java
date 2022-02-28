class Students{
	int m1,m2;
	void getmarks(int x,int y) {
		m1=x;
		m2=y;
	}
	void putmarks() {
		System.out.println("First : "+m1);
		System.out.println("Second : "+m2);
	}
}

interface Sport{
	int sp=6;
	void spmarks();
}

class Results extends Students implements Sport{
	int total;
	public void spmarks(){
		System.out.println("Sports marks : "+sp);
	}
	void disp() {
		putmarks();
		spmarks();
		total=m1+m2+sp;
		System.out.println("Total marks : "+total);
	}
}

public class MultipleInheritance {
	public static void main(String arg[]) {
		Results obj=new Results();
		obj.getmarks(89, 93);
		obj.disp();
	}

}
