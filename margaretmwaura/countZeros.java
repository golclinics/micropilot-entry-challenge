public class Main {
    public static void main(String[] args) {
        
        System.out.println("Hello World!");
        
        int[] values = new int[]{1, 0, 5, 6, 0, 2, 0, 0, 0 , 0};
        int result = countZeros(values);
        System.out.print(result);
    }
    
    public static int countZeros(int[] values){
        int count = 0;
        for(Integer digit : values){
            if(digit == 0){
                count++;
            }
        } 
        return count;
    }
}

