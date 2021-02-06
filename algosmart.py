'''
Program written for entry into GoL Clinics Mentorship
'''

def quadratic_function(a=1,b=2,c=1):
    '''
    This function takes three parameters: a,b and c.
    It then proceeds to calculate solutions of the corresponding 
    quadratic equation based on those parameters and return the greatest
    '''
    #Finding the two solutions
    x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    #Returning the greater solution
    return x1, x2
#first_entry = int(input("Enter the coefficient a: "))
#second_entry = int(input("Enter the coefficient b: "))
#third_entry = int(input("Enter the coefficient c: "))
    
def getX():
    '''
    function compares the values returned by the quadratic_function and finds the greatest
    '''
    #a, b = quadratic_function(first_entry,second_entry,third_entry)
    a,b = quadratic_function()
    return a if a>b else b
print(getX())
