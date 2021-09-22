

public int CountZeros(int []A){
   int zero_occurrence=0;
   int i=0;
   if(A.length==0)// if array is null/has no element return 0
       return zero_occurrence;

    Arrays.sort(A); // sort array first
    while((A[i]<1)){ // loop values below 1 after sorting
        if(A[i]==0)
        zero_occurrence++; // increment occurrence of zeros if current index has zero
       i++;
       if(i==A.length) 
           break;
   }


  return zero_occurrence;
}
