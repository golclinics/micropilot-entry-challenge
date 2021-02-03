using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace kayuyumwaura
{
    class kayuyumwaura
    {
        public static void Main()
        {
            //user input for values a, b, c
            Console.WriteLine("Enter any number for a: ");
            double a = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Enter any number for b: ");
            double b = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Enter any number for c: ");
            double c = Convert.ToDouble(Console.ReadLine());

            //calculate the value of the discriminant
            double discriminant = b * b - 4 * a * c;
            double x1, x2;

            //in this solution, we require that the discriminant be greater that zero so as to have two roots
            if (discriminant > 0)
            {
                x1 = (-b + Math.Sqrt(discriminant)) / (2 * a);
                x2 = (-b - Math.Sqrt(discriminant)) / (2 * a);

                double result = getX(x1, x2);

                Console.WriteLine($"The two roots are: {x1}, {x2}");
                Console.WriteLine($"The Max  value is: {result}");
            }
            else
            {
                Console.WriteLine("This result cant be used. Try again!");
            }


            Console.ReadLine();
        }

        //method to get the max value of the roots
        private static double getX(double x1, double x2)
        {
            double max = x1;
            if (x2 > max)
            {
                max = x2;
            }
            return max;
        }
    }
}
