def solve():
    input()
    arr= list(map(int, input().split()))
    arr = list(set(arr))

    arr.sort(reverse=True)

    if(len(arr) < 2 ):
        print("no second element found")
    else:
        print("second largest element is :",arr[1])
        
solve()