from math import sqrt

def JumpSearch(arr, key):
    n = len(arr)
    low = 0
    jump = int(sqrt(n))    #  jump size
    high = min(jump, n)  
   
    while low < n and arr[high - 1] < key:
        low = high
        high = min(low + jump, n)

    if low < n and arr[high - 1] >= key:
        return Linear(arr[low:high], key, low)    # linear search in the range

    return -1 

def Linear(arr, key, offset):
    for i in range(len(arr)):
        if arr[i] == key:
            return offset + i  
    return -1  


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
key = 11
result = JumpSearch(arr, key)
print(result)
