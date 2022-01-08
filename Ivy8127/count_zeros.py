def count_zeros(a):
    #define a counter variable
    count = 0
    if (len(a) == 0 or a == None):
        return "Empty list"
    for i in a:
        #loop through the list
        if i == 0:
            count = count + 1
    return count 

numbers = [0,1,0,0,3,4,5,6,0,0]
print(count_zeros(numbers))

       