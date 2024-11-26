def InterpolationSearch(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high and key >= arr[low] and key <= arr[high]:  
        pos = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])
        if arr[pos] == key:
            return pos
        
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1 

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
key = 11
result = InterpolationSearch(arr, key)
print(result)
       
