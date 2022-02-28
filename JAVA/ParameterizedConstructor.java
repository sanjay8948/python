class Rectangle{
	int length,width,A;
	Rectangle(int x,int y){
		length=x;
		width=y;
	}
	void RectArea() {
		A=length*width;
		System.out.println("Area of Rectangle is "+A);
	}
}
public class ParameterizedConstructor {
	public static void main(String args[]) {
		Rectangle obj=new Rectangle(10,15);
		obj.RectArea();
	}

}
