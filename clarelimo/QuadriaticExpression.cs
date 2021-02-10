using System;

namespace micropilot-entry-challenge
{
    class clarelimo
    {
        static void Main(string[] args)
        {
            Console.WriteLine(QuadriaticEquation("x2 - 6x + 5 = 0"));
            Console.WriteLine(QuadriaticEquation("x2 + 2x + 1 = 0"));
            Console.WriteLine(QuadriaticEquation("2x2 - 12x - 54 = 0"));
            Console.WriteLine(QuadriaticEquation("27x2 - 12 = 0"));
        }

        public static double QuadriaticEquation(string expression)
        {
            string[] newExpression = expression.Split(' ');
            string[] first = newExpression[0].Split('x'); 
            string[] second = newExpression[2].Split('x');
            if (first[0] == string.Empty)
            {
                first[0] = "1";
            }

            int a = int.Parse(first[0]);
            int b = 0;
            int c = 0;
            if (!newExpression[2].Contains('x'))
            {
                c = int.Parse(newExpression[1] + second[0]);
            }
            else
            {
                b = int.Parse(newExpression[1] + second[0]);
                c = int.Parse(newExpression[3] + newExpression[4]);
            }

            double pow = ((Math.Pow(b, 2)) - (4 * (a * c)));
            double sqrt = Math.Sqrt(pow);
            double addition = (-b + sqrt) / (2 * a);
            double subtraction = (-b - sqrt) / (2 * a);
            double ans = 0;

            if (addition > subtraction)
            {
                ans = addition;
            }
            else
            {
                ans = subtraction;
            }
            return ans;
        }
    }
}
