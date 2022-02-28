import java.util.Scanner;
public class OneDArray {
	public static void main(String arg[]) {
		int i,total=0;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter size of array : ");
		int n=sc.nextInt();
		int marks[]=new int[n];
		System.out.println("Array length : "+marks.length);
		System.out.println("Enter "+n+" elements ");
		
		for(i=0;i<n;i++){
			marks[i]=sc.nextInt();
		}
		System.out.print("\nArray is : ");
		for(i=0;i<n;i++) {
			System.out.print(marks[i]+"  ");
			total=total+marks[i];
		}
		System.out.println("\n Total : "+total);
	}

}
