/**
 * Returns the number of zero's in the array as count.
 *
 * The naming of the array adheres to the convention in the challenge though not a common practise in Java
 * to name variables or data structures such as Arrays starting with a capital letter.
 *
 * Assumptions made:
 * - The array is only of type integer.
 * - Zero is the accepted value when there are no zero's in the array.
 */


private int CountZeros(int[] A) {

    int count = 0;

    for(int i = 0; i < A.length; i++){
        if(A[i] == 0){
            count += 1;
        }
    }
    return count;
}