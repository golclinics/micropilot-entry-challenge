package com.goclinics.examples;
/*
    Java program to count zeros in an Array

    @author (Warren Ochibobo)

*/
class CountZeros{
    /*
    *
    * Count the number of zeros in an array
    *
    *
    * @param arr - Integer array from which zeros are to be counted
    * @param n - size of the arr
    *
    * @return - count of zeros in the array
    */
    public int countZeros(int [] arr, int n){
        //Variable to hold the count of zeros in arr
        int count = 0;

        //IF the array is empty, return 0
        if(n == 0) return count;

        //Loop via the array incrementing count when you encounter a zero
        for(int i = 0; i < n; i++){
            if(arr[i] == 0) count++;
        }

        //Return the value of count (number of zeros encountereds)
        return count;
    }
}