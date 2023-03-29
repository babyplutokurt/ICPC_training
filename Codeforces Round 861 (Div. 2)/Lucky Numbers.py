turn = int(input())


def f(lst):
    res = 0
    dic = {}
    for i in range(int(lst[0]), int(lst[1]) + 1, 1):
        nums = [int(cha) for cha in str(i)]
        res = max(res, max(nums) - min(nums))
        if res not in dic:
            dic[res] = i
        if res == 9:
            return i
    return dic[max(dic)]


for t in range(turn):
    lst = [i for i in input().split()]
    print(f(lst))
