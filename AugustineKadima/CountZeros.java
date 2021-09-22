import java.util.ArrayList;

public class CountZeros{
    public static void main(String[] args) {

        ArrayList<Integer> nums = new ArrayList<>();

        nums.add(1);
        nums.add(0);
        nums.add(5);
        nums.add(6);
        nums.add(0);
        nums.add(2);

        countZeros(nums);
    }

    public static int countZeros(ArrayList<Integer> A){
        int count = 0;
        for(int num : A){
            if(num == 0){
                count++;
            }
        }
        return count;
    }
}
