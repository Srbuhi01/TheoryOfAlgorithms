def Binary(arr, key):
    L = 0                  
    H = len(arr) - 1
    
    while L <= H:
        M = (L + H) // 2  # Mid index

        if arr[M] == key:  
            return M        # index of the key

        elif arr[M] < key:  
            L = M + 1      # Search in the right half

        else:  
            H = M - 1      # Search in the left half

    return -1
arr = [2, 4, 7, 8, 12, 45, 109, 123, 876, 1009, 4675]
key = 1090
result = Binary(arr, key)
print(result)
