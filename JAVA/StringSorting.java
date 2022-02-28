public class StringSorting {
	static String name[]= {"Sanjay","Neeraj","Ajay","Sanskar","Rakesh","Prashant"};      //1st method
	public static void main(String arg[]) {
		//String name[]= {"Sanjay","Neeraj","Ajay","Sanskar","Rakesh","Prashant"};         //2nd method
		int size=name.length;
		String temp=null;
		
		System.out.println("\n\tBefore Sorting");
		for(int i=0;i<size;i++) {
			System.out.println("\t"+name[i]);
		}
		for(int i=0;i<size;i++) {
			for(int j=i+1;j<size;j++) {
				if(name[i].compareTo(name[j])>0) {
					temp=name[i];
					name[i]=name[j];
					name[j]=temp;
				}
			}
		}
		System.out.println("\n\tAfter Sorting");
		for(int i=0;i<size;i++) {
			System.out.println("\t"+name[i]);
		}
	}

}
