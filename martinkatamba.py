#to get max root
#ax2 + bx + c = 0
# How  to run
#python3 martinkatamba.py

get_sqrt = lambda  x :  x ** 0.5
get_sq = lambda  x :  x ** 2
get_diff = lambda  x,y :  x - y
get_div = lambda  x,y :  x / y
get_4prod = lambda  x,y :  4 * x * y
get_2prod = lambda  x:  2 * x 

discriminant= lambda  a,b,c: get_sq(b)- get_4prod(a,c)

roots_type = lambda a,b,c : 1 if discriminant(a,b,c)>0 else 0  if discriminant(a,b,c) == 0 else -1

numinator= lambda a,b,c,d: -b +  d* get_sqrt(discriminant(a,b,c))

x1= lambda a,b,c : get_div(numinator(a,b,c,1),get_2prod(a))
x2= lambda a,b,c : get_div(numinator(a,b,c,-1),get_2prod(a))

get_roots = lambda a,b,c : [x1(a,b,c),x2(a,b,c)] if roots_type(a,b,c) ==1 else [x1(a,b,c)] if roots_type(a,b,c) ==0 else [x1(a,b,c),x2(a,b,c)] if roots_type(a,b,c) ==-1 else None    

get_max_root = lambda  a,b,c : get_roots(a,b,c)[0]

getX= lambda  a,b,c : get_max_root(a,b,c)

#a=1 ,b=2, c= 1 ,X= -1.0
print("when a=1 ,b=2, c= 1 then X =",getX(1,2,1))

#a=1 ,b=4, c= 1 ,X= -0.2679491924311228
print("when a=1 ,b=4, c= 1  then X =",getX(1,4,1))

#a=1 ,b=4, c= 5 ,X= -2+1j 
print("when a=1 ,b=4, c= 5 then X =",getX(1,4,5))
