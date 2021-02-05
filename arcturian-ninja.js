function getX(a,b,c){
 if(Math.round(a)===a && Math.round(b)===b && Math.round(c)===c){
    let discriminant,x1,x2;
    discriminant = (b*b) - (4*a*c);
    if(discriminant>0){
      x1 = (-b + Math.sqrt(discriminant))/(2*a);
      x2 = (-b - Math.sqrt(discriminant))/(2*a);
    }else{
      x1 = x2 = -b/(2*a);
    }
    return(x1>x2?x1:x2);
  }else{
    return 'Invalid Input';
  }
}