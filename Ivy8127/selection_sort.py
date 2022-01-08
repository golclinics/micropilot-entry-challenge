def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        #swap the current minimum with the unsorted array        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr    

data = [-2, 45, 0, 11, -9]
print(selectionSort(data))