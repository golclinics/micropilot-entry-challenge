import math  
  
# function for  roots 
def getX( a, b, c):  
  
    # calculating discriminant using formula 
    dis = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(dis))  
      
    # checking condition for discriminant 
    if dis > 0:  
        print(" the greatest value of X is: ")  
        x1 = (-b + sqrt_val)/(2 * a)
         
        x2 = (-b - sqrt_val)/(2 * a)
        
        
        if(x1>x2):
            x=x1
        else:
            x=x2
        print(x)
                
      
    elif dis == 0:  
        print(" real and same roots")  
        print(-b / (2 * a))  
      
    # when discriminant is less than 0 
    else: 
        print("Complex Roots")  
        print(- b / (2 * a), " + i", sqrt_val)  
        print(- b / (2 * a), " - i", sqrt_val)  
  
a = 4
b = 13
c = -44
  
# If a == 0 , incorrect eqution
if a == 0:  
        print("Enter a correct equation")  
  
else: 
    getX(a, b, c)