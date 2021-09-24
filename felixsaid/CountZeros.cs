public class int CountZeros(int[] A)
{
    int zerosCounter = 0;

    foreach(int item in A)
    {
        if(item == 0)
        {
            zerosCounter++;
        }
    }

    return zerosCounter;
}