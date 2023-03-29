turn = int(input())


def f(lst):
    res = 10
    dic = {}
    a = len(lst[0])
    b = len(lst[1])

    for i in range(int(lst[0]), int(lst[1]) + 1, 1):
        nums = [int(cha) for cha in str(i)]
        res = min(res, max(nums) - min(nums))
        if res not in dic:
            dic[res] = i
        if res == 0:
            return i
    return dic[min(dic)]


for t in range(turn):
    lst = [i for i in input().split()]
    print(f(lst))
