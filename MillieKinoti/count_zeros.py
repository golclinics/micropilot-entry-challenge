number_array = [0,5,6,0,0,6,7,0]

def countZeros(arr,number):
    return(arr.count(number))

number_of_zeros = countZeros(number_array, 0)
print('The are {} zeros in the array'.format(number_of_zeros))