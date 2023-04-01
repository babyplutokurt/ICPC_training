turn = int(input())
def f(n, nums):
    for j in range(n):
        if nums[j] <= j + 1:
            return 'YES'
    return "NO"

for t in range(turn):
    n = int(input())
    nums = [int(i) for i in input().split()]
    print(f(n, nums))

