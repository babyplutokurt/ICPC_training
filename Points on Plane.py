import math
turn = int(input())
for t in range(turn):
    num = int(input())
    if num == 1:
        print(0)
    else:

        i1, i2 = 0, 0
        sum1, sum2 = 0, 1
        n = math.sqrt(num // 4) // 1
        if (n ** 2) * 4 == num:
            pass
        else:
            n += 1
        s1 = n * 2 - 1

        num -= 1
        n = math.sqrt(num // 4) // 1
        if (n ** 2) * 4 == num:
            pass
        else:
            n += 1

        if num + 1 > 5 and (5 + 4 * ((n - 1) * n / 2)) > (num + 1):
            s2 = (n - 1) * 2
        else:
            s2 = n * 2
        print(min(round(s1), round(s2)))
