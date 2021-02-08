package sammymutahigicheru;

/*
* Write a function challengev1.sammymutahigicheru.CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array.
* For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.
* */
public class CountZeros {
    //Takes O(n) time and space complexity
    int countZeros(int[] A){
        int count = 0;
        for (int j : A) {
            if (j == 0) {
                count++;
            }
        }
        return count;
    }
}
