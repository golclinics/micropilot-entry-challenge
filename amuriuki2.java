
/*
 * @author amuriuki2
 */
import java.util.*;
import java.lang.Math;

public class amuriuki2 {
    static double a, b, c, x1, x2, determinant, detSqrt;
    
    static public double getX(double a, double b, double c) {
        //calculate determinant
        determinant = b * b - 4.0 * a * c;
        detSqrt = Math.sqrt(determinant);
        
        //check value of determinant and calculate values of x1 and x2
        if (determinant > 0.0) { //x1 and x2 are real and different
            x1 = (-b + detSqrt)/(2 * a);
            x2 = (-b - detSqrt)/(2 * a);
            if (x1 > x2) {
                System.out.println("The larger of the two values of X is x1: " + x1);
            } else {
                System.out.println("The larger of the two values of X is x2: " + x2);
            }
            
        } else if (determinant == 0.0) { //x1 and x2 are real and equal
            x1 = x2 = -b / (2.0 * a);
            System.out.println("Both roots are equal to: " + x1);
            
        } else { // x1 and x2 are not real
            System.out.println("The roots are not real");
        }
    return 0;
}
    
public static void main (String[] args) {
    
    //get values for the quadratic equation from the user
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter value of a: ");
    double a = scan.nextDouble();
    System.out.println("Enter value of b: ");
    double b = scan.nextDouble();
    System.out.println("Enter value of c: ");
    double c = scan.nextDouble();
    
    //pass the values to the getX function to calculate value/values of X
    amuriuki2.getX(a, b, c);
}
    
}
