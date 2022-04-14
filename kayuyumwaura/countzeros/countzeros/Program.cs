using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace countzeros
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] A = { 1, 0, 5, 6, 0, 2 };
            int count = 0;

            for (int j = 0; j <= (A.Length - 1); j++)
            {
                if (A[j] == 0)
                {
                    count++;
                }
            }
            Console.WriteLine(count);
            Console.ReadKey();
        }
    }
}
