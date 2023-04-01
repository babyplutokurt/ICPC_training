turn = int(input())

def magic(n):
    queue = [n]
    dic = {}
    while queue and queue[-1] != 1:
        curr = int(queue.pop(0))
        if (curr + 1) / 2 % 1 == 0:

            dic[int((curr + 1) / 2)] = curr
            queue.append((curr + 1) / 2)
        if (curr - 1) / 2 % 1 == 0:
            dic[int((curr - 1) / 2)] = curr
            queue.append((curr - 1) / 2)

    lst = [1]
    point = 1
    lst2 = []
    while point in dic and point != n:
        lst.append(dic[point])
        point = dic[point]
    for i in range(len(lst) - 1):
        if lst[i + 1] == lst[i] * 2 + 1:
            lst2.append(2)
        else:
            lst2.append(1)
    return len(lst) - 1, lst2


for t in range(turn):
    n = int(input())
    res = magic(n)
    if res[0] == 0:
        print(-1)
    else:
        print((res[0]))
        for i in range(len(res[1])):
            res[1][i] = str(res[1][i])
        print(" ".join(res[1]))
