let getX = (a,b,c) => {
    let discriminat, x1, x2;
   // check if a not equal to zero
   if (a === 0) {
      throw("Equation is Linear");
   }
   
  discriminat = Math.pow(b,2) - (4*a*c);

  if (discriminat < 0 ) {
      //not real numbers
     throw("values of x not real Numbers");
    }
  else if(discriminat === 0) {
    // The roots are equal
    x1 = x2 = -b / (2 * a);
  } else {
      x1 = (-b + Math.sqrt(discriminat)) / (2 * a);
      x2 = (-b - Math.sqrt(discriminat)) / (2 * a);
  }

  return Math.max(x1,x2);

}

/// Test function to compare the returns and expected output.
const Test = (a,b,c,output) => {
  let asn;
  try {
   asn = getX(a,b,c)
  } catch (e) {
    if (e === output) {
      console.log("Exception Thrown: ", e);
    };
  }
  if (asn === output){
    console.log(`Test passes: larger x value = ${output}`);
  }
}

// Test for all exectuction paths.

// Exception test.
// Test for when a = 0
Test(0,1,6,"Equation is Linear");
Test(5,2,2,"values of x not real Numbers");


/// a = 1, b = 6 , c = 5 : expected root x1 = -1, x2 = -5 : expected answer -1
Test(1,6,5,-1);

/// a = 1, b = -5, c = -14 : expected root x1 = -2, x2 = 7 : expected answer 7
Test(1,-5,-14,7);

/// a = 1, b = -25 , c = 0 : expected root x1 = 5, x2 = 5 : expected answer Nothing 
//there is 
Test(1,0,-25,"values of x are equal");



