function getX(a,b,c){
    let discriminant = 0;  //discriminant
    let squareRoot = 0;
    let r1 = 0;
    let r2=0;
     
      if(a === 0){
          return "Not a quadratic Equation,a should not be zero";
      }



    discriminant =  b*b - 4 * a *c;
 squareRoot = Math.sqrt(discriminant);
 if(discriminant > 0){
      r1 = (-b + squareRoot) / (2 * a);
      r2= (-b - squareRoot) / (2 * a);
      
        if(r1 > r2){
            return r1;
        }
        else{
            return r2;
        }
          
      
 }

 else if (discriminant === 0){
     r1 = r2 = -b/ (2 * a);
     return r1;
     
 }
 else{
       console.log("roots are not valid");
 }

      
}
getX(2,5,-3);
