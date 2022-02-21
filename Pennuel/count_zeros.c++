#include <bits/stdc++.h>

using namespace std; 
/*
    the function calculate the number of zeros in the list
    @param 1: the array containng the zeros 
    @param 2: the number of elements in the array
    @return: the number of zeros in the array
*/
int getZeroCount(int *arr, int n){
    int count=0;
    sort(arr,arr+n);
    for (int i=0;i<n;i++){
        if(arr[i]==0){
            count++;
        }
    }
    return count;
}

int main(){
    int intergerCount;  // the number A of the arrays
    cin >> intergerCount;
    int arr[intergerCount]; // the array containing the list

// loops through the array entering the values
    for (int i = 0; i < intergerCount;i++){
        cin >> arr[i];
    }
// prints the number of zeros
    cout <<endl<< getZeroCount(arr,intergerCount);
}