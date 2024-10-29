def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half) 

    return merge(left_sorted, right_sorted) 

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1 

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:]) 

    return sorted_arr 

arr = [4, -5, 0, 100, 89, 3, 10]
print(merge_sort(arr))
