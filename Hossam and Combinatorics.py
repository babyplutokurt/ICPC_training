turn = int(input())
for t in range(turn):
    n = int(input())
    nums = [int(i) for i in input().split()]
    max_num = max(nums)
    min_num = min(nums)
    max_diff = max_num - min_num
    a = nums.count(max_num)
    b = nums.count(min_num)
    if max_num != min_num:
        print(a * b * 2)
    else:
        print((a - 1) * b)