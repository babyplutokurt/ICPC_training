import math
turn = int(input())
for t in range(turn):
    lst = [int(i) for i in input().split()]
    if not lst[1] and not lst[3]:
        print(0)
    else:
        lst[0] *= lst[3]
        lst[2] *= lst[1]
        if not lst[0] and not lst[2]:
            print(0)
        elif not lst[0] or not lst[2]:
            print(1)
        elif lst[0] == lst[2]:
            print(0)
        elif (lst[0] / lst[2]) % 1 == 0 or (lst[2] / lst[0]) % 1 == 0:
            print(1)
        else:
            print(2)

