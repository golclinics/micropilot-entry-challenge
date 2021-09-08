# Amos Muraguri <GitHub: MurageMuraguri>
#
#Function to count zeros in an integer array
#returns count of zeros
def count_zeros(array = []):
    sorted_array = array.sort()

    zero_numbers = 0

    for x in sorted_array:
        while(sorted_array[x] == 0):
            zero_numbers += 1

    return zero_numbers



