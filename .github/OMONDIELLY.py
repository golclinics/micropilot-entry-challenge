import cmath

a = int(input("\n Enter the value of a:"))
b = int(input("\n Enter the value of b:"))
c = int(input("\n Enter the value of c:"))
def  getX(a,b,c):
#Solution for numerators
    check = (b**2) - (4*a*c)


    x1 =  (-b-cmath.sqrt(check))/(2*a)
    x2 =  (-b+cmath.sqrt(check))/(2*a)
   
# min & max for the roots
    if x1.real >x2.real:
        
        return x1.real
        
    else:
       return x2.real

print(getX(a,b,c))
      