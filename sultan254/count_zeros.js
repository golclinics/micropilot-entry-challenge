function CountZeros(A) {

    const count = []
    for (let i = 0; i < A.length; i++) {
      if (A[i] == 0) {
        count.push(A[i])
      }
      
    }
    return count.length
  
  }
  
  CountZeros(array);
  