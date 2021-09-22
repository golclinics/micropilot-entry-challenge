	public static int CountZeros(int[] listOfInts){
		int len = listOfInts.Length; //get the length of the array
		int numberOfZeros = 0; //initiate the number of zeros found to 0
		
        //loop through the array while looking for 0's
		for(int i=0; i < len; i++){
            
            //if a zero is found, increment numberOfZeros
			if(listOfInts[i] == 0){
				numberOfZeros++;
			}
		}
		return numberOfZeros; //return the number of 0's found
	}