/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package countzeros;
import java.util.*;
/**
 *
 * @author Caren Achieng
 */

//A Java Program Which Accepts an array of integer values and returns the sum of zeros in the array

public class CountZeros {
   
    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
       
        //Getting Array Size from user
        Scanner size=new Scanner(System.in);
        System.out.println("Enter the size of your Array"+"\n");
        int arraySize=size.nextInt();
       
        //Initialize the array
      int arr[]=new int[arraySize];
     
      //Capture array values from the user
      Scanner values=new Scanner(System.in);
      System.out.println("Enter your array values"+"\n");
      for(int i=0;i<arr.length;i++){
          arr[i]=values.nextInt();
      }
     
      //Find the total number of zeros in the array
      int sum=0;
      for(int j=0;j<arr.length;j++){
          if(arr[j]==0){
              sum=sum+1;
          }else{
              sum=sum;
          }
      }

      //Print the result
      System.out.println("The number of zeros in your array is: " + sum);
    }
}
