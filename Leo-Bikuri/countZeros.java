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
    }
}
