def count_zeros(A):
    zero_count = 0
    for i in A:
        if int(i) == 0:
            zero_count += 1
    return zero_count



if __name__=="__main__":
    print(count_zeros([1,0,4,5,0]))
    print(count_zeros(["0",0,4,0,0]))