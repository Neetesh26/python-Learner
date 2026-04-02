def solve(arr1 , arr2):
    n =  len(arr1)
    if n != len(arr2):
        return print("both arr mustbe equal...")
    
    for i in range(n):
        if arr1[i:] + arr1[:i] == arr2:
            left =i 

            right = n-i

            print("Left Rotations:", left)
            print("Right Rotations:", right)

            return min(left,right)
    return -1

print("Minimum:", solve([1,2,3,4,5], [3,4,5,1,2]))
print("Minimum:", solve([1,2,3,4,5], [4,5,1,2,3]))
print("Minimum:", solve([1,2,3], [2,3,1]))

