function countZeros (){
    let myArray =[1,0,5,6,0,2]
    let count=0;
    for (let i=0; i<myArray.length; i++){
        if (myArray[i]===0)
        count ++
    }
    console.log ('myArry has' + ",", count, "zeros" )
}
countZeros()