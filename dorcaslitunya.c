#include <stdio.h>
#include <stdlib.h>
#include <math.h>
double getx(double a,double b, double c)
{
    double discriminant=(b*b)-(4*a*c);
    double root1=0,root2=0;


    if(discriminant>0)
    {
        root1=(-b+sqrt(discriminant))/(2.0*a);
        root2=(-b-sqrt(discriminant))/(2.0*a);
        if(root1>root2)
        {
            return root1;
        }
        else
        {
            return root2;
        }
    }
    else if(discriminant==0)
    {
        root1=(-b)/(2.0*a);
               root2=root1;
               return root1;
    }
          else
    {
        double real_part=(-b)/(2.0*a);
        double imaginary_part=(sqrt(-discriminant))/(2.0*a);
        printf("root1 = %.2lf+%.2lfi ", real_part, imaginary_part);
        return 0;
    }

}





int main()
{
    int a=0,b=0,c=0;


    printf("Please enter only the integer value of a,b,c of the quadratic equation you want to solve");
    printf("\na:");
    scanf("%d",&a);
    printf("\nb:");
    scanf("%d",&b);
    printf("\nc:");
    scanf("%d",&c);
    printf("The result of %dx^2 + %dx + %df is:%.4f",a,b,c,getx(a,b,c));
    return 0;
}




