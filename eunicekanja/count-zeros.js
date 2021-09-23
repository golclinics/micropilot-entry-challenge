function CountZeros(arr){
    const newArr=arr.filter((item)=>{
        return item===0;
    })
    return newArr.length;
}