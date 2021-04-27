#A function that takes in an array of integers.
#Return the number of times the value 0 appears into the array.
#the function should return the number of zeros
def CountZero(A):
   x = A.count(0)
   return x

l = [1, 0, 8, 9, 0, 6, 0, 6, 0]
count = CountZero(l)
print (count)