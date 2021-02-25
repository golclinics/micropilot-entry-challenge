public class Main {

    public static void main(String[] args) {
        Numbers num = new Numbers();
        int[] input = new int[]{1, 0, 0, 0, 5, 6, 0};
        System.out.println(num.countZero(input));
    }
}

class Numbers {

    public int countZero(int[] input) {
        int count = 0;
        for (int i = 0; i < input.length; i++) {
            if (input[i] == 0) {
                count++;
            }
        }
        return count;
    }
}
