var NumberOfZeros = function(array) {   //define your variable
    var i = 0;
    array.forEach(function(z) {        //try to identify how many zeros are there in the array
      if (z === 0) i++;
    });
    return i;
  }
  
  var count = NumberOfZeros([4, 0, false, 5, 0]);
  console.log(count);     //display the result
  

