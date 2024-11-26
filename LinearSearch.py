def Linear(arr, key):
    ind = -1
    for i in range(len(arr)):
        if arr[i] == key:
            ind = i
    return ind

arr = [2, 6, 9, 10, 12, -8, 4]
key = 10
result = Linear(arr,key)
print(result)
