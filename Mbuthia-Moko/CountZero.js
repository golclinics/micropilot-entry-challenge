package counterzero;

public class CounterZero {

    /**
     * @param A
     * @return
     */
    public static int CountZeros(int A[]) {
        int counter = 0;
        for (int i = 0; i < A.length; i++) {
            if (A[i] == 0) {
                counter++;
            }
        }

        return counter;
    }

    public static void main(String[] args) {
        int[] array;
        array = new int[]{1, 0, 5, 6, 0, 2};
        System.out.println(CountZeros(array));

    }
}
