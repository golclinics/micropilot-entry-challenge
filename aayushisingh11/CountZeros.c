#include <stdio.h>

void main()
{
    int arr[50], n, i, positive = 0, negative = 0, zero = 0;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter array elements-\n");
    for (i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    for (i = 0; i < n; i++)
    {
        if (arr[i] > 0)
            positive++;
        else if (arr[i] < 0)
            negative++;
        else
            zero++;
    }
    printf("Number of zeros: %d", zero);
