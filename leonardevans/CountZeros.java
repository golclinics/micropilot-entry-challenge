public class CountZeros {
    public static void main(String[] args) {
        int [] array = {1, 0, 5, 6, 0, 2};
        System.out.println(countZeros(array));
    }

    public static int countZeros(int[] numbersArray) {
        //set the number of zeros to zero
        int numberOfZeros = 0;

        //loop through the array
        for (int number : numbersArray
        ) {
            //check if the current number is zero
            if (number == 0) {
                //increment number of zeros
                numberOfZeros++;
            }
        }
        return numberOfZeros;
    }
}
