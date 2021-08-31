#include<iostream>
using namespace std;

int CountZeros(int A[], int size)
{
    int count =0;
    for(int i=0; i<size; i++)
    {
        if(A[i] == 0)
        {
            count++;
        }
    }
    cout<<"Number of zeroes: ";
    
    return count;
}

int main()
{
    int A[8] = {1,0,5,6,0,2, 0, 0};
    cout<<CountZeros(A, 8)<<endl;
    
}