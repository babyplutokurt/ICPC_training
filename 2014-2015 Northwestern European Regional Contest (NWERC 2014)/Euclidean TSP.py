import math
import decimal
decimal.getcontext().prec = 100

lst = [float(i) for i in input().split()]
tep = math.sqrt(2)
dom = 10 ** 9

n = float(lst[0])
p = float(lst[1])
s = float(lst[2])
v = float(lst[3])


def get(c):
    return (decimal.Decimal(n * decimal.Decimal((math.log2(n)) ** (c * tep))) / (p * dom) + (1 + 1 / c) * s / v)


r = 10 ** 6
l = 0
while r - l > 10 ** -10:
    lmid = (l + r) / 2
    rmid = (lmid + r) / 2
    if get(lmid) > get(rmid):
        l = lmid
    else:
        r = rmid
print(get(l), l)
