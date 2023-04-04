turn = int(input())


def judge(n, x, y):
    m2 = min(n - y, y - 1)
    r1 = n / 2 - m2
    if n / 2 - r1 + 1 <= x <= n / 2 + r1:
        return m2 + 1
    else:
        return min(n - x, x - 1) + 1


for t in range(turn):
    lst = [int(i) for i in input().split()]
    n = lst[0]

    print(abs(judge(n, lst[1], lst[2]) - judge(n, lst[3], lst[4])))
