#include <stdio.h>

void main()
{
    int CountZero[50], n, i, positive = 0, negative = 0, zero = 0;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter array elements-\n");
    for (i = 0; i < n; i++)
        scanf("%d", &CountZero[i]);

    for (i = 0; i < n; i++)
    {
        if (CountZero[i] > 0)
            positive++;
        else if (CountZero[i] < 0)
            negative++;
        else
            zero++;
    }
    printf("Number of zeros: %d", zero);
}
