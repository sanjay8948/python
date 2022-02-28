public class StringComparing1 {
	public static void main(String arg[]) {
		String str1="Sanjay";
		String str2="Kumar";
		String str3="sanjay";
		String str4="Sanjay5";
		String str5="Sanjay3";
				
		
		System.out.println(str1.compareTo(str1));
		System.out.println(str1.compareTo(str2));
		System.out.println(str1.compareTo(str3));
		System.out.println(str1.compareTo(str1+str2));
		System.out.println(str4.compareTo(str5));
		
	}

}
