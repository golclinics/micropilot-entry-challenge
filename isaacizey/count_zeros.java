import java.util.ArrayList;
public class HelloWorld{

     public static void main(String []args){
        
        int[] list = {0, 20,0, 30, 40}; 
          
          ArrayList<Integer> newList = new ArrayList<Integer>();
        for(int i =0; i< list.length; i++)
        {
            if(list[i] == 0)
            {
                newList.add(list[i]);
            }
        }
        
        System.out.println(newList.size());
     }
}