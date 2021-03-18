using System;				
public class CountZero
{
	public static void Main()
	{
		Console.WriteLine(CountHelper(new int[]{1, 0, 5, 6, 0, 2}));
	}
	
	public static int CountHelper(int [] numbers)
	{
		if (numbers.Length == 0) {
			return 0;
		}
		int count = 0;
		
		foreach(int num in numbers) {
			if(num == 0) {
				count++;
			}
		}
		return count;
	}
}
