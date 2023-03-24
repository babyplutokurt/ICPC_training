turn = int(input())
for t in range(turn):
    n = int(input())
    mons = [int(i) for i in input().split()]
    mons.sort()
    supp = 0
    res = 0
    for i in range(n):
        if mons[i] - supp < 1:
            continue
        if mons[i] - supp == 1:
            supp += 1
        else:
            res += (mons[i] - supp - 1)
            supp += 1
    print(res)
