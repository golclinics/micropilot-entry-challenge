
public class CountZeros {
    public static void main(String[] args) {
        int[] input = {1, 0, 5, 6, 0, 2,100,006,90};
        System.out.println(numberOfZeros (input)); 
    }

    public static int numberOfZeros(int[] input){
        int countOfZeros = 0;
        for (int num : input) {
            if (num == 0) {
                countOfZeros ++;
            }
        }
        return countOfZeros;
    }
}