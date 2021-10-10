using System;
public class MicropilotChallenge
{
    public static int CountZeros(int[] A)
    {
        int count = 0;
        if (A.Length == 0 || A == null)
        {
            return 0;
        }

        for (int i = 0; i < A.Length; i++)
        {
            if (A[i] == 0)
                count++;
        }

        return count;
    }

    public static void Main(string[] args)
    {
        int[] A = new int[] { 1, 0, 5, 6, 0, 2 };
        Console.WriteLine(CountZeros(A));
    }
}