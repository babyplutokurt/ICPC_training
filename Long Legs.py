import math

turn = int(input())
for t in range(turn):
    nums = [int(i) for i in input().split()]
    a = nums[0]
    b = nums[1]
    if a < b:
        a, b = b, a
    fac = a // b
    if a // b == 1:
        g = math.gcd(a, b)
        if g == 1:

