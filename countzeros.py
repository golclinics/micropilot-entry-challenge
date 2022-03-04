def count_zeros(list):
    count = 0
    for number in list:
        if number == 0:
            count += 1

    return count

print(count_zeros([1, 0, 5, 6, 0, 2]))
print(count_zeros([10, 15, 0, 3, 0, 2, 8, 0]))
print(count_zeros([3, 2, 6, 8]))
print(count_zeros([2, 4, 1, 0]))