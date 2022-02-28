public class StringCompare2 {
	public static void main(String arg[]) {
		String str1="Hello";
		String str2="Hello";
		String str3="Sanjay";
		String str4="HELLO";
		
		System.out.println("\tstr1\t"+str1);
		System.out.println("\tstr2\t"+str2);
		System.out.println("\tstr3\t"+str3);
		System.out.println("\tstr4\t"+str4);
		
		System.out.println("\tstr1 equals str2 "+str1.equals(str2));
		System.out.println("\tstr1 equals str3 "+str1.equals(str3));
		System.out.println("\tstr1 equals str4 "+str1.equals(str4));
		System.out.println("\tstr3 equals str4 "+str3.equals(str4));
		System.out.println("\tstr1 equals str4 "+str1.equalsIgnoreCase(str4));
	}

}
