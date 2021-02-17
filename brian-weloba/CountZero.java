import java.util.Arrays;
import java.util.Scanner;

public class CountZero {
  public static void main(String[] args) throws Exception {
    Scanner sc = new Scanner(System.in);
    System.out.println("Welcome");
    while (true) {
      System.out.println(" Do you want to? \n 1. (Continue)  \n 2. (Quit)");
      System.out.println(" ");

      int navigate = sc.nextInt();
      sc.nextLine();

      if (navigate == 1) {

        System.out.println("How many elements are in the array?(Integer only):");
        int num = sc.nextInt();
        int[] numArray = new int[num];
        System.out.println("Enter each array element and press enter(Integer only):");

        for (int i = 0; i < num; i++) {
          numArray[i] = sc.nextInt();
        }

        int count = 0;
        for (int element : numArray) {
          if (element == 0) {
            count++;
          }
        }
        System.out.println("There are " + count + " zeros in " + Arrays.toString(numArray));
      } else if (navigate == 2) {
        System.exit(0);
        sc.close();
      } else {
        System.out.println("Invalid choice");
      }

    }
  }

}