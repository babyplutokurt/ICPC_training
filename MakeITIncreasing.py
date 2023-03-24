Turn = int(input())


def count_(nums, n):
    if n > nums[-1] + 1:
        return -1
    count = 0
    if nums[-1] == 0:
        return -1
    else:
        for i in range(n - 2, -1, -1):
            while nums[i] >= nums[i + 1]:
                nums[i] = nums[i] // 2
                count += 1
                if nums[i] == 0 and i > 0:
                    count = -1
                    return count
        return count


for turn in range(Turn):
    n = int(input())
    nums = [int(i) for i in input().split()]
    print(count_(nums, n))


