function countZero(A){
    
    let z = [];
    for(i=0; i<A.length; i++){
        if(A[i] === 0){
            z.push(A[i]);
        }
        

    }
console.log(z.length);

}
let myX = [1, 0, 5, 6, 0, 2] ;//testcase1
let b =[1,3,0,0,8,12,9,0]; //testcase2
countZero (myX);
countZero (b);