class Student{
	int roll;
	void getroll(int x) {
		roll=x;
	}
	void putroll() {
		System.out.println("Roll no. is "+roll);
	}
}

class TestMarks extends Student{
	int m1,m2;
	void getmarks(int x,int y) {
		m1=x;
		m2=y;
	}
	void putmarks() {
		System.out.println("Marks of Test-1 are "+m1);
		System.out.println("Marks of Test-2 are "+m2);
	}
}

class Result extends TestMarks{
	int total;
	void disp() {
		putroll();
		putmarks();
		total=m1+m2;
		System.out.println("Total marks are "+total);
	}
}
public class MultilevelInheritance {
	public static void main(String arg[]) {
		Result obj=new Result();
		obj.getroll(101);
		obj.getmarks(81, 89);
		obj.disp();
	}

}
