public int CountZeros(int[] A)
{
    var arraylistValues = new List<int>();
    for(int i=0; i< A.Length, i++) { |

        if (!arraylistValues.Contains(A[i]) and (A[i].Equals(0))
        {
            arraylistValues.Add(A[i])
        }
            
    }
    return arraylistValues.Count

}

public int getX(double a, double b, double c)
{
    
    double x1, x2 = 0.0;
    x1 = (((-1) * b) + (Math.Sqrt(Math.Sqr(b) - (4 * a * c))))/(2*a);
    x2 = (((-1) * b) - (Math.Sqrt(Math.Sqr(b) - (4 * a * c)))) / (2 * a);

    if (x1 > x2)
    {
        return x1;
    }
    else
    {
        return x2
    }
}

