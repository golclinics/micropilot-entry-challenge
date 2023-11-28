int CountZero(int A[], int size)
{
    int count = 0;

    for (int i = 0; i < size; i++)
    {
        if (A[i] == 0)
        {
            count++;
        }
    }

    return count;
}