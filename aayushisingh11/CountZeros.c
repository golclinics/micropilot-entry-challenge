#include <stdio.h>
int CountZeros(int arr[], int low, int high)
{
    if (high >= low)
    {
        
        int mid = low + (high - low)/2;
        if (( mid == 0 || arr[mid-1] == 1) && arr[mid] == 0)
            return mid;
  
        if (arr[mid] == 1) 
            return CountZeros(arr, (mid + 1), high);
        else  
            return CountZeros(arr, low, (mid -1));
    }
    return -1;
}
  
int countZeroes(int arr[], int n)
{
 
    int first = CountZeros(arr, 0, n-1);
  
    if (first == -1)
        return 0;
  
    return (n - first);
}
  
/* Driver program to check above functions */
int main()
{
    int arr[] =   {1, 1, 1, 0, 0, 0, 0, 0, 0};
    int n = sizeof(arr)/sizeof(arr[0]);
    printf("Count of zeroes is %d", countZeroes(arr, n));
    return 0;
}