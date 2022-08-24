def count_zeros(arr):
    zeros = [each for each in arr if each == 0]
    print(len(zeros))
count_zeros([1,2,3,0,0,5])