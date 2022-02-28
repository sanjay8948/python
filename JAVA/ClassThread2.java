class Cthread implements Runnable{
	public void run() {
		for(int i=1;i<=7;i++) {
			System.out.println("C thread");
		}
	}
}
public class ClassThread2 {
	public static void main(String arg[]) {
		Cthread t=new Cthread();
		Thread obj=new Thread(t);
		obj.start();
		for(int i=1;i<=7;i++) {
			System.out.println("Main thread");
		}
	}

}
