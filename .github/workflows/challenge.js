function getx(a, b, c) {
    var x = (-1 * b + Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
    var x2 = (-1 * b - Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
    if(x>x2){
      console.log(`X is greatest in ${x}  than ${x2}`);
    }
    else if(x2>x){
       console.log(`X is greatest in ${x2}  than ${x}`);

    }
    else{
      console.log("they are equal");
    }
  
}
console.log(getx(a,b,c));