using System;
using System.Linq;

namespace CountZeros
{
    class Program
    {
        static void Main(string[] args)
        {
            string val;
            Console.Write("Define Array Size: ");
            val = Console.ReadLine();
            int ArraySize = Convert.ToInt32(val);

            Console.WriteLine("Input [" + ArraySize + "] Integers");
            Console.WriteLine("--------");

            string[] array = new string[ArraySize];

            for(int i = 0; i < array.Length; i++)
            {
                array[i] = Console.ReadLine();
            }

            Console.WriteLine("--------");
            Console.WriteLine("Your array: " + "[{0}]", string.Join(",", array));

            string check = "0";
            int count = array.Count(s => s == check);
            Console.WriteLine("Occurences: " + count);
        }
    }
}