class Athread extends Thread{
	public void run() {
		for(int i=1;i<=10;i++) {
			System.out.println("From thread A "+i);
		}
		System.out.println("Exit from A");
	}
}

class Bthread extends Thread{
	public void run() {
		for(int i=1;i<=10;i++) {
			System.out.println("From thread B"+i);
		}
		System.out.println("Exit from B");
	}
}

public class ClassThread1 {
	public static void main(String arg[]) {
		Athread obja=new Athread();
		Bthread objb=new Bthread();
		
		obja.start();
		objb.start();
	}

}
