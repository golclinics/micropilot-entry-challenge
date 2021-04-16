class CountZeros {
    public static void main(String[] args) {
        System.out.println(countZeros(new int[]{1, 0, 5, 6, 0, 2}) ==2);
    }

    public static int countZeros(int[] inputs) {
        int zeros = 0;
        for (int input : inputs) {
            if (input == 0) {
                zeros += 1;
            }
        }
        return zeros;
    }
}