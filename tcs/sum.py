def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    total = 0

    for i in range(len(arr)):   # safer
        total = total + arr[i]

    print("total sum",total)

solve()