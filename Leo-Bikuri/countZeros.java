public class countZeros {
    
    public int CountZeros(int A[]){
        int counter = 0;
        for(int x = 0;x < A.length; x++){
            if(A[x]==0){
                counter++;
            }
        }
        return counter;
    }
    public static void main(String args[]) {
        countZeros count = new countZeros();
        int[] arr = {0, 3, 0, 5, 0, 6, 2};
        System.out.println(count.CountZeros(arr));
    }
}
