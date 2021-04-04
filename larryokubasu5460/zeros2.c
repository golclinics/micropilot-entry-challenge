
//  Write a function CountZeros(A) that takes in an array of integers A, and returns the number of 0's in that array.
// For example, given [1, 0, 5, 6, 0, 2], the function/method should return 2.

#include <stdio.h>

int countZeros(int a[]);

int main()
{
    int array[] = {1, 0, 5, 6, 0, 2};
    int zeros = countZeros(array);
    printf("Number of zeros in array is %d ", zeros);
    return 0;
}

int countZeros(int a[])
{

    int count = 0;
    int value = 0;
    for (int i = 0; i < 6; i++)
    {
        if (a[i] == value)
        {
            count++;
        }
    }
    return count;
}
