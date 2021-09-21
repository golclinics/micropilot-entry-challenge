using System;

public class EntryChallenge
{
    public int CountZeros(int[] A)
    {
        int count = 0;
        foreach (int number in A)
        {
            if (number == 0)
            {

                count++;
            }
        }

        return count;
    }
}