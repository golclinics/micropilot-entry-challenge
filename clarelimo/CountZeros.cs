using System;

namespace CountZeros
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] Arr = { 1,0,5,6,0,2};
            int[] Arr2 = { 0, 0, 0, 0, 0, 0 };
            int[] Arr3 = { };
            int[] Arr4 = { 2,30, 5, 6};
            Console.WriteLine(CountZero(Arr));
            Console.WriteLine(CountZero(Arr2));
            Console.WriteLine(CountZero(Arr3));
            Console.WriteLine(CountZero(Arr4));

        }
        public static int CountZero(int[] A){
            int n = A.Length;
            int count = 0;
            int prev = 0;
            Array.Sort(A);
            for (int i = 0; i < n; i++)
            {
                if (A[i] == prev)
                {
                    count++;
                }
            }
            return count;
        }
    }
}
