//a function CountZeros(A) that takes in an array of integers A, 
//and returns the number of 0's in that array 

// Arrays = [1, 0, 5, 0, 6, 0, 8, 0,2]

function CountZeros(A) {

    var zeros = [];
    for(var i = 0; i < A.length; i ++){
    	if(A[i] === 0) {
        	zeros.push(A[i]);
        }
    }
    console.log(zeros.length);
    console.log(CountZeros);
}

CountZeros([1, 0, 5, 0, 6, 0, 8, 0,2])
