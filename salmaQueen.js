function getx(a, b, c) {
    var result = (-1 * b + Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
    var result2 = (-1 * b - Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
    if(result>result2){
      console.log(`X is greatest in ${result}  than ${result2}`);
    }
    else if(result2>result){
       console.log(`X is greatest in ${result2}  than ${result}`);

    }
    else{
      console.log("they are equal");
    }
  
}
getx(a,b,c);