turn = int(input())
for t in range(turn):
    n = int(input())
    nums = [int(i) for i in input().split()]
    pos = 0
    neg = 0
    for num in nums:
        if num >= 0:
            pos += 1
        else:
            neg += 1

    line1 = [i for i in range(1, pos + 1)] + [j for j in range(pos - 1, pos - neg - 1, -1)]
    line2 = [1, 0] * min(pos, neg) + [i for i in range(1, abs(pos - neg) + 1)]
    print(*line1)
    print(*line2)