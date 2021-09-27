public class Main{
    public static int countZeros(int[] arr, int n){
        int count = 0;
        for(int i=0; i<n; i++)
            if(arr[i] == 0){
                count++;
            }
        return count;
    }

    public static void main(String[] args){
        int[] arr = new int[]{0,0,1,2,3,4};
        int n = arr.length;
        System.out.println(countZeros(arr,n));
    }
}
