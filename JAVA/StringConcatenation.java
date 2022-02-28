public class StringConcatenation {
	public static void main(String arg[]) {
		String str1="Sanjay"+"Kumar";
		String str2=str1+"Azamgarh";
		String str3=str1+str2;
		int no=100;
		String str4=no+str1;
		String str5=no+4+str2+no+4;
		
		//By concat() method
		
		String str6=str1.concat("Nishad");
		String str7=str1.concat(str2);
		
		
		System.out.println(str1);
		System.out.println(str2);
		System.out.println(str3);
		System.out.println(str4);
		System.out.println(str5);
		System.out.println(str6);
		System.out.println(str7);
	}

}
