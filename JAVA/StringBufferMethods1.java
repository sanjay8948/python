public class StringBufferMethods1 {
	public static void main(String arg[]) {
		
		StringBuffer s1=new StringBuffer("Sanjay");
		System.out.println("\tcharacter at position 3 is "+s1.charAt(2));
		
		StringBuffer s2=new StringBuffer("java");
		System.out.println("\tBefore using setCharAt() method the string is   "+s2);
    	s2.setCharAt(2,'l');
		System.out.println("\tAfter using setCharAt() method the string is   "+s2);
		
	}

}
