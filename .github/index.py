def CountZeros(A):
    count=0
    for i in A:
        if i==0:
            count+=1
    return count



if __name__ == '__main__':
    print(CountZeros([1, 0, 5, 6, 0, 2]))
