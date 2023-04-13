/**
 * CountZeros - a function that counts the number of zeros in a given array
 * @A: array being checked
 * @index: size of array
 * @count: count of zeros in an array
 * */
 
 int CountZeros(int A[], int index)
 {
     int count = 0;
     
     for (int i = 0; i < index; i++)
     {
         if (A[i] == 0)
         count++;
     }
     
     return count;
 }
