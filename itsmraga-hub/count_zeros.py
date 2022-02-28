list_to_check = [1, 0, 5, 6, 0, 2]


def count_zeroes(list_of_numbers):
    number_of_zeroes = 0
    for i in list_of_numbers:
        if i == 0:
            number_of_zeroes += 1

    return number_of_zeroes


print("The value is: " + str(count_zeroes(list_to_check)))
