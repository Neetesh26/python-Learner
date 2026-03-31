def solve():
    input()
    arr = list(map(int,input().split()))
    min_val = float("inf")
    for num in arr:
        if num < min_val: 
            min_val = num
    
    print("minimum number is : " , min_val)
solve()
