using System;

namespace rosianah
{
    class rosianah
    {
        static int getX(int a,int b, int c)
        {
            int x1 = (int)(-b + Math.Sqrt(Math.Pow(b,2)) - (4*a*c)) / (2*a);
            int x2 = (int)(-b - Math.Sqrt(Math.Pow(b, 2)) - (4 * a * c)) / (2 * a);
            return Math.Max(x1, x2);
        }
        static void Main(string[] args)
        {            
            Console.WriteLine(getX(2,3,4));
        }
    }
}
