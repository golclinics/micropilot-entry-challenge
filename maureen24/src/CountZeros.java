
public class CountZeros {
	
	public static int countZeros(int[] A) {
		int count = 0;
		
		for(int i = 0; i < A.length; i++) {
			if(A[i] == 0) {
				count = count + 1;
			}
		}
		
		return count;
	}

	public static void main(String[] args) {
		int [] array = new int [] {1, 0, 5, 6, 0, 2};
		
		System.out.println(countZeros(array));
	}

}
