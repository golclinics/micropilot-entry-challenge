using System;

namespace innocentkhaemba
{
    public class Solution
    {
        int CountZeros(int[] a)
        {
            int count = 0;

            for (int r = 0; r < a.Length; r++)
            {
                if (a[r] == 0)
                    count++;
            }

            return count;
        }

        static void Main(string[] args)
        {
            Solution solution = new Solution();

            int[] a = new int[] { 1, 0, 5, 6, 0, 2 };

            Console.WriteLine(string.Format("There are {0} zeros in array a", solution.CountZeros(a)));

            Console.WriteLine("Press any key to exit...");

            Console.ReadLine();
        }
    }
}