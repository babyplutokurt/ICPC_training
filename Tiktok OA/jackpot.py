def jackpot(x):
    if x == 1:
        return -1
    elif x > 1:
        res = 0
        while x % 10 != 7:
            x = 2 * x - 1
            res += 1
        return res
    else:
        res = 0
        while x % 10 != 3:
            x = 2 * x - 1
            res += 1
        return res

for t in range(5):
    a = int(input())
    print(jackpot(a))