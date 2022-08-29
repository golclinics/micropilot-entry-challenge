#include<stdio.h>
#define N 14
int main()
{
  int a[N], result;
  printf("Enter %d integer numbers\n", N);
result=CountZeros(a);
    printf("\n The no. of Zeros are : %d\n", result);

    return 0;
}

int CountZeros(int A){

  int a[N], i, z = 0;

    for(i = 0; i < N; i++)
        scanf("%d", &a[i]);

    for(i = 0; i < N; i++)
    {
        if(a[i] == 0)
            z++;
        else
            continue;
    }
    return z;
}
