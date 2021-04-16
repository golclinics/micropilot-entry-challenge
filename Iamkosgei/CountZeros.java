import  java.util.*;
class CountZeros {
    public static void main(String[] args) {
        System.out.println(countZeros(new int[]{1, 0, 5, 6, 0, 2}) ==2);
    }

    //using loops
    public static int countZeros(int[] inputs) {
        int zeros = 0;
        for (int input : inputs) {
            if (input == 0) {
                zeros += 1;
            }
        }
        return zeros;
    }

    //using collection
    public static int countZeros2(int[] inputs){
        return (int) Arrays.stream(inputs).filter(c -> c==0).count();
    }
}