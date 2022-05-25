function countZeros(A){

    return A.filter(zero => zero === 0).length
  }
  
  console.log(countZeros([2,3,0,2,0,1,0]))
  
  //3