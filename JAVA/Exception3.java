public class Exception3 {
	public static void main(String arg[]) {
		int valid=0,invalid=0;
		int no;
		
		for(int i=0;i<arg.length;i++) {
			try {
				no=Integer.parseInt(arg[i]);
			}
			catch(NumberFormatException e) {
				invalid=invalid+1;
				System.out.println("Invalid number = "+arg[i]);
				continue;
			}
			valid=valid+1;
		}
		System.out.println("Valid = "+valid);
		System.out.println("Invalid = "+invalid);
	}

}
