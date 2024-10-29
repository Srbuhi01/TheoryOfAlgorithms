def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) - 1]
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)
arr = [4, 6, 7, -9, 0, 2, 3, 4, 55]
print(quicksort(arr))
