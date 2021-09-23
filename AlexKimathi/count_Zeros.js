const A = new Array (1,0,0,6,8,0);
const CountZeros = A.filter(function(counts){
    return counts == 0;   
});
console.log(CountZeros.length);