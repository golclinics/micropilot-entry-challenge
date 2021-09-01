/*
  Project: Entry Challenge #1
  Date: 1 Sept 2021
*/

#include <iostream>

int CountZeros(int array[6])
{
    int zeroCount = 0;
    
    for(int i = 0; i < 6; i++)
    {
        if(array[i]==0)
            zeroCount++;
    }
    
    return zeroCount;
}

int main()
{
    int A[6] = {1, 0, 5, 6, 0, 2};
    std::cout << "Zero count: " << CountZeros(A) << std::endl;
    
    return 0;
}
