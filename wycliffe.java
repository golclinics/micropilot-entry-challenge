public class QuadraticFormula {
    public static void main(String args[]) {
        System.out.println(getX(1, 6, -14));
    }

    public static double getX(int a, int b, int c) {
        double root = Math.sqrt(Math.pow(b, 2) - (4 * a * c));
        if (!Double.isNaN(root)) {
            double x = ((-1 * b) + root) / (2 * a);
            double x2 = ((-1 * b) - root) / (2 * a);
            if (x < x2)
                return x2;
            else
                return x;
        }else{
            throw new IllegalArgumentException("The equation provided evaluates to a NaN");
        }
    }
}
