from itertools import count


mylist = [0, 5, 8, 9, 0, 1, 0, 4, 0, 12]

def CountZeros(A):
    count = 0;
    for i in A:
        if(i==0):
            count+=1;
    return count;

print(CountZeros(mylist))