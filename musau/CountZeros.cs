public int CountZeros(int[] A)
{
    int count = 0;
    for (int i=0; i<A.Length-1; i++)
    {
        if (A[i] == 0)
            count += 1;
    }
    return count;
}