function CountZeros(){
    var  array_values = [1,0,5,6,0,2];
    var count = 0;
    for (i = 0;i < array_values.length;i++){
        if(array_values[i] === 0)
        count++
    }
    console.log("There are" + " " + count + "  " + "zeros in the array")
 }
 CountZeros()