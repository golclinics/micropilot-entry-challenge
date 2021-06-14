public static class CountZeros{
    public static int CountZeros(int[] a)
    {
        int zerosCount = 0;

        try
        {
            int i = 0, j = a.Length -1;

            for (i = 0; i <= j; i++)
            {
                if (a[i].Equals(0))
                {
                    zerosCount++;
                }

                if (a[j].Equals(0) && !j.Equals(i))
                {
                    zerosCount++;
                }

                j--;
            }
            return zerosCount;
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error occured while counting zeros."+ Environment.NewLine + ex.ToString());
            return 0;
        }
    }
}