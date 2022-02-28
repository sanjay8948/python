public class StringBufferClass {
	public static void main(String arg[]) {
		
		StringBuffer s1=new StringBuffer();
		System.out.println("\tLength "+s1.length());
		System.out.println("\tCapacity "+s1.capacity());
		
		StringBuffer s2=new StringBuffer(20);
		System.out.println("\tLength "+s2.length());
		System.out.println("\tCapacity "+s2.capacity());
		
		
		StringBuffer s3=new StringBuffer("Sanjay");
		System.out.println("\tString is "+s3);
		System.out.println("\tLength "+s3.length());
		System.out.println("\tCapacity "+s3.capacity());
		
		
	}

}
