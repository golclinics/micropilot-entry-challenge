Array.prototype.count=function CountZeros(A){
    var c=0;
    for(let i=0;i<this.length;i++){
        if(this[i]===A){
            c++;

        }
    }
return c;
    
}
var A=[1,0,4,3,2,0,4,0];
console.log(A.count(0));