using System;

    public class Program
    {
        //Program to solve a quadratic equation and print the greater of the two roots
		
		//Main function 
		public static void Main(string[] args)
        {
			//Declaring quadratic equation coefficients
			
            Console.WriteLine("Enter the value a:");
            int a = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter the value b:");
            int b = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter the value c:");
            int c = Convert.ToInt32(Console.ReadLine());
			
			//Calling the quadratic formula function
            Console.WriteLine(findX(a, b, c));
        }
		
		//Quadratic formula function
        public static double findX(int a, int b, int c)
        {
            double sqrRoot = Math.Sqrt(Math.Pow(b, 2) - (4 * a * c));
			
			//Checking square root is a real number
            if (!Double.IsNaN(sqrRoot))
            {
                double x1 = ((-1 * b) + sqrRoot) / (2 * a);
                double x2 = ((-1 * b) - sqrRoot) / (2 * a);

                Console.WriteLine("The greater root is:");
				
				//Check the greater number
                if (x1 < x2)
                    return x2;
                else
                    return x1;
            }
            else
            {	
				//Throw an exception for an imaginary root
                throw new ArgumentException("This equation results to an imaginary number! Try Again");
            }
        }
    }
