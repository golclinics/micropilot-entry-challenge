import java.util.Scanner;

class CountZeroes {
    public static void main(String[] args) {
        int n, i = 0;
        Scanner A = new Scanner(System.in);
        System.out.print("Enter no. of numbers you want in array:");
        n = A.nextInt();
        int a[] = new int[n];
        System.out.println("Enter all the numbers needed; one at a time:");
        for(i = 0; i < n; i++)
        {
            a[i] = A.nextInt();
        }
        
        
        for(i = 0; i < n; i++)
        {
            if(a[i] == 0)
            {
            }
        }
      System.out.println();
    }
  }