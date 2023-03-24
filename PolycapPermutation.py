Turn = int(input())
for i in range(Turn):
    n = int(input())
    a = [int(a) for a in input().split()]
    p = []
    if max(a) != a[0] and max(a) != a[-1]:
        print(-1)
    else:
        if max(a) == a[0]:
            p.append(a[0])
            a= a[1:]
        else:
            p.append(a[-1])
            a = a[:-1]
        while a:
            p = [a[0]] + p
            a = a[1:]
        print(p)


