//array
A = [1,4,5,0,0,0]


function countZeros(arr){
    let count=0;
    for(let i=0; i<arr.length; i++){
        if(arr[i]==0){
            count++
        }
    }
    return count;
}

countZeros(A)