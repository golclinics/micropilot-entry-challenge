let A = [1,3,0,4,0,9,7,0,8];

function CountZeros(arr){
    let count = 0;
    for(i=0; i < arr.length; i++){
        if(arr[i]===0){
            count++;
        }
    }
    return count;
}
CountZeros(A);