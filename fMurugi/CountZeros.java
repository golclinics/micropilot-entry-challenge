package fMurugi;

public class CountZeros {

    public static int countZeros(int[] nums){
        int count=0;
        for(int i=0;i< nums.length;i++){
            if(nums[i]==0){
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int [] nums ={1,0,5,6,0,2};

        int results = countZeros(nums);
        System.out.println(results);
    }
}
