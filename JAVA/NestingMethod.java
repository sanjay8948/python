class Nesting{
	int m,n;
	
	Nesting(int x,int y){
		m=x;
		n=y;
	}
	
	int largest() {
		if(m>n) {return m;}else {return n;}
	}
	
	void disp() {
		int ans=largest();
		System.out.println("Largest value is "+ans);
	}
}
public class NestingMethod {
	public static void main(String arg[]) {
		Nesting obj=new Nesting(3,9);
		obj.disp();
	}

}
