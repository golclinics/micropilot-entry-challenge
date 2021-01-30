function getX(a,b,c)
{ var a = parseInt(a),b=parseInt(b), c=parseInt(c);
var m=Math.sqrt((b*b)-(4*a*c));
var x1=(-b+(+m))/(2*a),x2=(-b-m)/(2*a);
return(x1>x2)/x1:x2;
}
