class Cube{
	static int cube(int x) {
		return (x*x*x);
	}
}
public class StaticMember {
	public static void main(String arg[]) {
		int a=Cube.cube(5);
		System.out.println("Cube is "+a);
	}

}
