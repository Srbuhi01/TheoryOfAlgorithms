def insertion_sort(Arr):
    for i in range(1, len(Arr)):
        j = i
        while j > 0 and Arr[j-1] > Arr[j]:
            Arr[j-1], Arr[j] = Arr[j], Arr[j-1]
            j -= 1
    return Arr  

Arr = [4, 6, 0, 2, 9, 3, 7, 1]
sorted_Arr = insertion_sort(Arr)
print(sorted_Arr)

