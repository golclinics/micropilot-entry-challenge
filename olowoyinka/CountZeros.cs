using System;

namespace Clincs
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number of array elements you want");

            int ArrayLength = Convert.ToInt32(Console.ReadLine());

            int[] arrnumber = new int[ArrayLength];

            for (int i = 0; i < ArrayLength; i++)
            {
                Console.WriteLine($"Insert a number to the {i} index element");

                arrnumber[i] = Convert.ToInt32(Console.ReadLine());
            }

            int numberofO = CountZeros(arrnumber);

            Console.WriteLine($"The number of O's is {numberofO}");
        }

        static int CountZeros(int[] A)
        {
            int countA = 0;

            for (int i = 0; i < A.Length; i++)
            {
                if (A[i] == 0)
                {
                    countA++;
                }
            }

            return countA;
        }
    }
}
