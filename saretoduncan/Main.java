
public class Main{
    public static void main(String[] args){
        int[] numArr = {1, 0, 5, 6, 0, 2,0,0,0};// test array
        int noOfZeros=countZeros(numArr);// call counter method
        System.out.println(noOfZeros);

    }
    public static int countZeros(int[] num){//counter method
            int results=0;
                for(int i=0; i<num.length;i++){
                    if(num[i]==0){
                        results++;
                }
        }
        return results;

    }
}