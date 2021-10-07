def countZeros(arr):
    count=0
    for elm in arr:
        if elm==0:
            count+=1
    return count
def main():
    print(countZeros([1,2,0,0,0,4]))
    print(countZeros([1,2,0,5,0,4]))
    print(countZeros([1,0,0,0,0,4]))
    print(countZeros([1,9,1,2,0,4]))

main()
