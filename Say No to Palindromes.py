lst = [int(i) for i in input().split()]
s = input()


def diff(s, a):
    res = 0
    for i in range(len(s)):
        if s[i] != a[i]:
            res += 1
    return res


for i in range(lst[1]):
    num = [int(i) for i in input().split()]
    s_ = s[num[0] - 1: num[1]]
    com = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    result = float('Inf')
    for c in com:
        compare = (num[1] - num[0] + 1) // 3 * c + c[0: (num[1] - num[0] + 1) % 3]
        result = min(result, diff(s_, compare))
    print(result)
