import java.util.Scanner;

public class

countZeros {
    int myArray[];

    public static void main(String [] args) {
        countZeros jeckly = new countZeros();
        jeckly.myArray = new int[5];


        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter  " + jeckly.myArray.length + " numbers:");

        for (int i = 0; i < jeckly.myArray.length; i++) {
            System.out.println("Enter number " + (i + 1) + ":");
            jeckly.myArray[i] = scanner.nextInt();
        }
        System.out.println("You entered:");
        for (int figures : jeckly.myArray) {
            System.out.print(figures);

        }
        int jecklyCount = jeckly.countZeros();
        System.out.println ();
        System.out.println("The number of zeros is " + jecklyCount);

        scanner.close();

    }
        public int countZeros(){
            int counter = 0;
            for (int figures : myArray) {
                if (figures == 0) {
                    counter++;
                }

            }
return counter;
        }


}
