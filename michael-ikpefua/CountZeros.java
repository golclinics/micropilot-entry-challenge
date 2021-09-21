class CountZeros {

    public static void main(String[] args) {
        int[] A = {1,0,5,6,0,2};
        int output = CountZeros(A);

        System.out.println(output);
    }

    public static int CountZeros(int[] A) {
        int noOfZeros = 0;

        for (int i = 0; i < A.length; i++) {
            if (A[i] == 0) {
                noOfZeros += 1;
            }
        }

        return noOfZeros;
    }
}