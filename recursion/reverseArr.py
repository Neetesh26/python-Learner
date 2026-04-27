# ip [1 2 3 4 5]
# op [5 4 3 2 1]

def reverseArr(arr ,i ,j):
    if i >= j:
        return arr
    
    arr[i],arr[j]=arr[j],arr[i]
    return reverseArr(arr , i+1 ,j-1)


    
arr = [1,2,3,4,5,2]
i = 0
j=len(arr)-1
print(reverseArr(arr, i, j))