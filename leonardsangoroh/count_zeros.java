package count_zeros;

/**
 *
 * @author leesangoroh
 */
public class count_zeros {
    
    /* Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array. 
       For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.*/

    
    static int CountZero(int [] arr) {
        
        //length stores the length of the array
        int length = arr.length;
        
        //count stores the number of times zero is present in the array
        int count = 0;
        
        for (int i = 0; i< length ; i++) {
            
            if (arr[i] == 0) {
                count++;
            }
        }
        
        return count;
    }
            
            
    public static void main(String[] args) {
        
        int [] myArr = {4,0,5,6,7,0,9,9,3,0};
        
        System.out.println(CountZero(myArr));
        
        
    }
    
}
