import java.util.Scanner;

public class count_zeros{
    //Function that returns the number of times zero occurs
    public static int countZeros(int[] arr, int n){
        int count = 0;
        for(int i=0; i<n; i++)
            if(arr[i] == 0){
                count++;
            }
        return count;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        //To declare and initialize the array size
        int a;
        System.out.println("Enter the array size");
        a = scanner.nextInt();

        //To input the integers in the array
        int arr[] = new int[a];
        System.out.println("Input the elements of the array");
        for (int i = 0; i<a; i++){
            arr[i] = scanner.nextInt();
        }
        System.out.println("Zero occurs" + countZeros(arr,a) + "times");

    }
}
