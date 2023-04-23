#include <stdio.h>

int main (void)
{
    //declaring data members
    int counter, arrSize, i;

    printf("Enter the number of elements for the array: ");
    scanf("%d", &arrSize);
    
    int arr[arrSize];

    //enter number of elements equal to arrSize
    printf("Enter any %d numbers\n", arrSize);
    //fill array with input
    for (i = 0; i < arrSize; i++)
    {
        scanf("%d", &arr[i]);
        if (arr[i] == 0)
        {
            counter++;
        }else{
            printf("There are no zeros");
        }
    }
    printf("The number of zeros is %d\n", counter);
    return (0);
}
