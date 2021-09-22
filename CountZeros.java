public class CountZeros {
    
    public static int countZeros(){
    
     int count =0;
     int[] numbers = {1, 0, 5, 6, 0, 2};    
     for (int i=0; i <numbers.length; i++){
         if (numbers[i]==0){
             count++;
         }
     }
     
     return count;
    
}
    
    public static void main(String[] args){
        System.out.println(countZeros());
    }
}