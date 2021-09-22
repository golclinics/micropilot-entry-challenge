using System;

namespace CountZeros
{
    public class Program
    {
        static void Main(string[] args)
        {
            var counter = new Counter();
            int[] numArray = { 1, 0, 5, 6, 0, 2, 0, 4, 4, 0 };

            counter.CountZeros(numArray);
        }  
    }

    public class Counter
    {
        public void CountZeros(int[] numArray)
        {
            int count = 0;
            for (int i = 0; i < numArray.Length; i++)
            {
                if (numArray[i] == 0)
                    count += 1;
            }
            Console.WriteLine($"The number zeros in the array  is {count}");
        }
    }
}
