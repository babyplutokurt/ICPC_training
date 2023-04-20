for i in range(int(input())):
    n = int(input())
    o = [3 * int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    res = 0
    for i in range(n - 1, -1, -1):
        if o[i] < b[i]:
            res = i + 1
    if res:
        print(res)
    else:
        print(-1)