

public class abdimayow {

	public static double getx(double a ,double b,double c) {
		double x=0;
		double x1=0;
		double x2=0;
		
		double mb =-b;
		double sq =Math.sqrt(Math.pow(b,2)-4*a*c); 
		
		x1=(mb-sq)/2*a;
		x2=(mb+sq)/2*a;
				
		
		if(x1>x2) {
			x=x1;
		}else {
			x=x2;
		}
		return x;
	}
	
	public static void main(String [] args) {
		
		double ans=getx(1,-5,-14);
		System.out.println(ans);
		
	}
}
