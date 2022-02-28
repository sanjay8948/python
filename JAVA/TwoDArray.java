import java.util.Scanner;
public class TwoDArray {
	public static void main(String arg[]) {
		int i,j,diagonal=0;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter number of row and column : ");
		int row=sc.nextInt();
		int col=sc.nextInt();
		int a[][]=new int [row][col];
		System.out.println("Enter "+(row*col)+" elements ");
		
		for(i=0;i<row;i++) {
			for(j=0;j<col;j++) {
				a[i][j]=sc.nextInt();
			}
		}
		System.out.println("\nThe matrix is ");
		for(i=0;i<row;i++) {
			for(j=0;j<col;j++) {
				System.out.print(a[i][j]+"\t");
			}
			System.out.println();
		}
	/* if we want to calculate Sum of diagonal then*/
		for(i=0;i<row;i++) {
			for(j=0;j<col;j++) {
				if(i==j) {
					diagonal=diagonal+a[i][j];
				}
			}
		}
		System.out.println("\nSum of diagonal is : "+diagonal);
	
	}
	
}
