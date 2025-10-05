# bubble sort 
l = [9,8,4,2,5,98,34]
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
print(l)        

