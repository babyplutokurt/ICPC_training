turn = int(input())
for t in range(turn):
    lst = [int(i) for i in input().split()]
    if lst[3] < lst[1]:
        print(-1)
    elif lst[3] - lst[1] < lst[2] - lst[0]:
        print(-1)
    else:
        a = lst[3] - lst[1]
        lst[0] += a
        b = lst[0] - lst[2]
        print(a + b)