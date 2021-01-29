public class ProfNandaa {

   public double getX(int a, int b, int c) {
       double x;
       double x2;
       double x1;
       final double v = (Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
       x1 = (-b + v);
       x2 = (-b - v);

       x = Math.max(x1, x2);
       return x;
   }
}