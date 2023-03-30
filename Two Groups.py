turn = int(input())
for t in range(turn):
    n = int(input())
    nums = [int(i) for i in input().split()]
    a = 0
    b = 0
    for num in nums:
        if num >= 0:
            a += num
        else:
            b += num
    print(abs(a + b))