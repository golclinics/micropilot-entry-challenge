import java.util.Scanner;

public class ciradu2204 {

    public static double getX(double a, double b, double c){

        //if a = 0 then there is no quadratic equation
        if(a == 0){
            return 0;

        }
         // find b^2 - 4ac
        double delta = Math.pow(b, 2) - 4*a*c;

        // find the squareRoot of b^2 - 4ac
        double sqr = Math.sqrt(delta);

        //find the first x
        double x1 = (-b + sqr)/2*a;

        //find the second x
        double x2 = (-b - sqr)/2*a;

         // return the maximum number between x2 and x1
          return Math.max(x1, x2);
    }


    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        double a = sc.nextDouble();
        double b = sc.nextDouble();
        double c = sc.nextDouble();

        //print the largest x
        System.out.println(getX(a, b,c));


    }


}
