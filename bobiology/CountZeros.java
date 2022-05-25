public class CountZeros {

	public static void main(String[] args) {
		int[] A = {1, 0, 5, 6, 0, 2};
		System.out.println(totalZeros(A));

	}
	
	static int totalZeros(int[] nums) {
		int count = 0;
		for(int num : nums) {
			if(num == 0)
				count ++;
		}
		return count;
	}

}
