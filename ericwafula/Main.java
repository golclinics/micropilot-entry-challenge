public class Main {
    public static void main(String[] args) {
        int[] numbers = {1, 0, 5, 6, 0, 2, 0};
        int zeros = CountZeros(numbers);
        System.out.println(zeros);
    }

    public static int CountZeros(int[] numbers){
        int counter = 0;

        for(int number : numbers){
            if (number == 0){
                counter++;
            }
        }
        return counter;
    }
}