import java.util.*;
import java.lang.*;
public class CountZeros{
  public static double quadEqn(int a,int b,int c){
    double sqroot = Math.sqrt(Math.pow(b,2)-4*a*c);
    double numerator =  Math.max(-b+sqroot,-b-sqroot);
    double denominator = 2*a;
    double ans = numerator/ denominator;
    System.out.println(ans);
    return ans;
  }

  public static void main(String[] args) {
    quadEqn(2,15,5);
    quadEqn(1, 4, 1);

  }
}