  public int CountZeros(int[] A)
  {
            int count = 0;

            foreach (var item in A)
            {
                if (item == 0)
                {
                    count++;
                }
            }

            return count;
    }