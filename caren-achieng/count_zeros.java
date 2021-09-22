/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package count_zeros;

/**
 *
 * @author Caren Achieng
 */

public class count_zeros {

    public int CountZeros(int A[])
    {
         int sum=0;
      for(int j=0;j<A.length;j++){
          if(A[j]==0){
              sum=sum+1;
          }else{
              sum=sum;
          }
      }
      return sum;
    }
  
    
    public static void main(String args[]) {
        count_zeros sum = new count_zeros();
        int[] arr = {1, 0, 5, 6, 0, 2};
        System.out.println(sum.CountZeros(arr));
    }
}
