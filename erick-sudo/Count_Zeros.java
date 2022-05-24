public class Count_Zeros {

	public static int CountZeros(int arr[]){
		for(int i=0 , count=0; i<arr.length; i++) {
			if(arr[i]==0) count++;
			if(i==arr.length-1) return count;
		}
		return 0;
	}

	public static void main(String...args) {
		System.out.println("The array has "+CountZeros(new int[] {41, 0, 51, 36, 99, 0, 67, 0, 0, 56, 3, 0, 23, 0})+" 0's");
	}
}