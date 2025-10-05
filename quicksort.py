def quick_sort(arr, start, end):
    if(start<end):
        pivot_idx = partition(arr, start, end)
        quick_sort(arr, start, pivot_idx-1)
        quick_sort(arr, pivot_idx+1, end)


def partition(arr, start, end):
    idx = start - 1
    pivot = arr[end]
    for i in range(start, end):
        if arr[i] <= pivot:
            idx += 1
            temp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = temp
    idx += 1
    temp = arr[end]
    arr[end] = arr[idx]
    arr[idx] = temp
    return idx


arr = [6, 3, 4, 8, 7, 2, 9, 5]
start = 0
end = len(arr) - 1
quick_sort(arr, start, end)

for i in range(end):
    print(arr[i],end="")
