using System;

namespace Quadratic
{
    class Program
    {
        static void Main(string[] args)
        {
            
            Console.WriteLine(getX(1,5,6));
        }

        public static double getX(double a=1, double b=1, double c=0)
        {
            double x1, x2;
            
            double firstPart =Math.Sqrt((b * b)-(4 * a * c));

            b *= -1;

            x1 = ((b) - firstPart) / (2 * a);

            x2 = ((b) + firstPart) / (2 * a);

            return Math.Max(x1, x2);
        }
    }
}
