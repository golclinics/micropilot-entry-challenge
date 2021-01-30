public class GetX {
    public static void main(String [] args) {
        getX(2D, -11D, 14D);
    }
    
    public static void getX(double a, double b, double c) {
        double discriminant = (Math.pow(b, 2) - 4*a*c);
        double x1 = (-b + Math.sqrt(discriminant)) / (2*a);
        double x2 = (-b - Math.sqrt(discriminant)) / (2*a);

        // condition one: a cannot be equal to zero
        if (a == 0) {
            System.out.println("a cannot be zero!");
            return;
        }

        // condition two: eliminate complex solutions
        if (discriminant < 0) {
            System.out.println("Complex solution resulted!");
            return;
        }

        double maxValue = Math.max(x1, x2);
        System.out.println(maxValue);
        return;
    }
}