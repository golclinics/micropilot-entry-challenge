using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BRIANMWAMBIA
{
    public class CountZeros
    {
       public static int countZeros(int[] num)
        {

            int count = 0;
            //loop through the array checking for zero

            for (int i = 0; i<num.Length; i++)
            {
                //increment count every time this returns true
                if (num[i] == 0)
                {
                    count +=1;
                }

            } Console.WriteLine(count);
            return count;
        }

    }
}
