public class StringBufferMethods3 {
	public static void main(String arg[]) {
		
		StringBuffer s1=new StringBuffer("Sanjay");
		System.out.println("Before using append() method string is \t"+s1);
		s1.append(" Kumar");
		System.out.println("After using append() method the string is \t"+s1);
		
		
		StringBuffer s2=new StringBuffer("I Kumar");
		System.out.println("Before using insert() method the string is \t\t"+s2);
		s2.insert(2,"am Sanjay ");
		System.out.println("After using insert() method string is \t\t"+s2);
	}

}
