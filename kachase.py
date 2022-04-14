# Python program to find roots of quadratic equation 
import math 
def getVariablex():
    #getting the values of a,b,c
     a= float(input("Enter the value of a:"))
     b= float(input("Enter the value of b:"))
     c= float(input("Enter the value of c:"))
     #calculating the value of the discriminant
     discriminant = b * b - 4 * a *c
     sqrt_dis = math.sqrt(abs(discriminant))
     if discriminant>0 :
         print("real and different roots")
         ans1=(b+ sqrt_dis)/(2*a)
         
         ans2=(-b- sqrt_dis)/(2*a)
         print(ans1)
         print(ans2)
         if ans1>ans2:
             print("The largest value of x is:{} " .format(ans1))
         else:
             print("The largest value of x is:{} " .format(ans2))
         
        
     elif discriminant==0 :
         print("real and equal roots")
         ans1=(-b /(2*a))
         print("The values of x are equal :{} " .format(ans1))
       
     else:
         print("real and complex roots")
         ans1=(- b / (2 * a), " + i", sqrt_dis)
         ans2=(- b / (2 * a), " - i", sqrt_dis)
         print(ans1)
         print(ans2)
         if ans1>ans2:
             print("The largest value of x is:{} " .format(ans1))
         else:
             print("The largest value of x is:{} " .format(ans2))
        

# Driver Program 


getVariablex()


        

   
