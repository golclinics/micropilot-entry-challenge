def QuickSort(arr):
    elements = len(arr)

    # Base case
    if elements < 2:
        return arr

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp  # Brings pivot to it's appropriate position

    left = QuickSort(arr[0:current_position])  # Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position + 1:elements])  # sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right  # Merging everything together

    return arr


def CountZeros(A):
    print(len(A))
    if len(A) < 2:
        if A[0] == 0:
            return 1
        else:
            return 0

    sorted_array = QuickSort(A)
    return next((i for i, x in enumerate(sorted_array) if x), None)  # x!= 0 for strict ma


array_to_be_sorted = [1, 0, 5, 6, 0, 2]
print("Original Array: ", array_to_be_sorted)
print("Num zeros: ", CountZeros(array_to_be_sorted))
