a = [1, 2, 3, 4, 5, 10]


def searchInsert(nums, target: int) -> int:
    left, right = 0, len(nums) - 1
    if target <= nums[left]:
        return 0
    if target > nums[right]:
        return right + 1
    if target == nums[right]:
        return right
    while left < right:
        mid = left + (right - left) // 2
        if nums[left] == target:
            return left
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            if mid - 1 > 0 and nums[mid - 1] < target:
                return mid
            else:
                right = mid - 1
        else:
            if mid + 1 <= len(nums) - 1 and nums[mid + 1] > target:
                return mid + 1
            else:
                left = mid + 1
    return left + 1

print(searchInsert(a, 2))