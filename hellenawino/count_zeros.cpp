#include <iostream>
using namespace std;

int countZeros(int A[], int arraySize)
{
  int numberOfzeros = 0, i;
  for (i = 0; i < arraySize; i++)
  {
    if (A[i] == 0)
    {
     numberOfzeros++;
    }
  }

  return numberOfzeros;
}

int main()
{
  int A [] = {1, 0, 5, 6, 0, 2, 8, 7, 0, 7, 5, 0, 1, 0, 0, 0, 0, 0, 0, 0};
  int arraySize = sizeof(A)/sizeof(A[0]);
  int numberOfZeros = countZeros(A, arraySize);
  cout << "Value is : " << numberOfZeros;
}
