public class StringClass {
	public static void main(String arg[]) {
		String str=new String();       //Empty String
		String str1="Sanjay";
		String str2=new String("Kumar");
		char name[]= {'S','A','N','J','U','B','A','B','A'};
		String str3=new String(name);
		String str4=new String(str3);
		String str5=new String(name,5,4);
		
		System.out.println(str);
		System.out.println(str1);
		System.out.println(str2);
		System.out.println(name);
		System.out.println(str3);
		System.out.println(str4);
		System.out.println(str5);
		System.out.println(str2.length());
		
	}

}
