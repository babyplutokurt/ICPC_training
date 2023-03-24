turn = int(input())
for t in range(turn):
    n = int(input())
    lst = [int(i) for i in input().split()]
    if n == 1:
        print(0)
    else:
        res = []
        res += [max(lst[1:]) - lst[0]]
        res += [lst[-1] - min(lst[:-1])]
        res += [max([lst[i] - lst[i + 1] for i in range(len(lst) - 1)])]
        res += [lst[-1] - lst[0]]
        print(max(res))


