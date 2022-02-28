public class StringBufferMethods2 {
	public static void main(String arg[]) {
		
		StringBuffer s1=new StringBuffer("Sanjay");
		System.out.println("Before using delete() method the String is\t"+s1);
		s1.delete(2,5);
		System.out.println("After using the delete() method the String is\t"+s1);
		
		
		StringBuffer s2=new StringBuffer("Kumar");
		System.out.println("Before using deleteCharAt() method the String is\t"+s2);
		s2.deleteCharAt(2);
		System.out.println("After using the delete() method the String is\t"+s2);
	}

}
