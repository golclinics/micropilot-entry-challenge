#include <stdio.h>
//Program written by Lincoln Theophilus - tiprock- network
//My prototype function
int count_zeros(int a[20]);

int main()
{
    printf("Enter 20 numbers including others as zeros\n");
    //First Counter
    int i;
    //My array
    int num[20];
    //Looping to enter the numbers
    for(i=0;i<=20;i++)
    {
        printf("Enter your %d number: ",i);
        scanf("%d",&num[i]);
        printf(" \n");//Skip line for @after entry
    }

    //Display the numbers
    //Second Counter
    int x;

    printf("Numbers that you entered: \n");
    for(x=0;x<=20;x++)
    {

        printf("%d \t",num[x]);

    }

    //Calling the count_zeros() function given the prototype
    //User-defined: Accepts Value and does not return value back to main
    printf(" \n");
    printf(" \n");
    count_zeros(num);

    return 0;
}

//Function
int count_zeros(int a[20])
{
    //Loop to count the number of zeros I have in my array A
    //First counter
    int y;
    int zero_counter=0;
    for(y=0;y<=20;y++)
    {
      if(a[y]!=0)continue;
      //Counter checking
      printf("Element %d in the array is: %d\n",y,a[y]);
      zero_counter++;
    }

    printf("The number of zeros in A are: %d",zero_counter);

}

