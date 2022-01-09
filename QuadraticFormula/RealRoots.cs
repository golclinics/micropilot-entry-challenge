using System;

namespace QuadraticFormula
{
    public class RealRoots
    {
        public static double GetX(double a, double b, double c)
        {
            /*            _______
               x = −b ± √b^2−4ac
                   _____________
                       2a
           */
            if (a == 0) // equation is not quadratic.
            {
                return -1;
            }
            double x1;
            double x2;

            // Calculate determinant value (b^2)-(4ac)
            double determinant = (b * b) - (4 * a * c);
            double sqrt = Math.Sqrt(determinant);

            if (determinant > 0) //  there are two real roots
            {
                x1 = (-b + sqrt) / (2 * a);
                x2 = (-b - sqrt) / (2 * a);
            }
            else if (determinant == 0) // there is one real root.
            {
                return (-b + sqrt) / (2 * a);
            }
            else // Invalid (there are two complex roots)
            {
                return -1;
            }
            return Math.Max(x1, x2);
        }
    }
}
