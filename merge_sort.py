def merge_sort(arr,st,end):
    if st < end:
        mid = (st + end)//2
        merge_sort(arr,st,end)
        merge_sort(arr,mid+1,end)
        sorting(arr,st,mid,end)
def sorting(arr,st,mid,end):
    temp = []
    i = st 
    j = mid+1
    while i<=mid and j <=end:
        if arr[i]<=arr[mid]:
            temp.append(arr[i])
            i +=1
        else:  
            temp.append(arr[j])  
            j+=1
    while i<=mid:
        temp.append(arr[i])
        i +=1
    while j <=end:
        temp.append(arr[j])  
        j+=1
    for idx in range(st,end):
        arr[idx+st] = temp[idx]    
arr = [6,5,54,57,2,3,98,8,9]
st = 0
end = len(arr) - 1
merge_sort(arr,st,end)

