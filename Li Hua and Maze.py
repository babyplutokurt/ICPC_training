turn = int(input())
for t in range(turn):
    lst = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    if (nums[0], nums[1]) == (1, 1) or (nums[0], nums[1]) ==(1, lst[1]) or (nums[0], nums[1]) ==(lst[0], 1) or (nums[0], nums[1]) ==(lst[0], lst[1]):
        print(2)
    elif (nums[2], nums[3]) == (1, 1) or (nums[2], nums[3]) == (1, lst[1]) or (nums[2], nums[3]) == (lst[0], 1) or (nums[2], nums[3]) == (lst[0], lst[1]):
        print(2)
    elif nums[0] == 1 or nums[0] == lst[0]:
        print(3)
    elif nums[1] == 1 or nums[1] == lst[1]:
        print(3)
    elif nums[2] == 1 or nums[2] == lst[0]:
        print(3)
    elif nums[3] == 1 or nums[3] == lst[1]:
        print(3)

    else:
        print(4)