def fancyPairPair(pairs, k1, k2):
    res = 0
    pairs.sort()
    hard_cap = k1 - pairs[0][0]
    right = binarySearch(pairs, hard_cap, 0)
    if right == -1:
        return 0
    print(pairs[0: right + 1])
    k2_lst = [num[1] for num in pairs[0: right + 1]]
    k2_lst.sort()
    for i in range(right + 1):
        soft_cap = k2 - pairs[i][1]
        curr = binarySearch2(k2_lst, soft_cap)
        if pairs[i][1] <= soft_cap:
            res += curr - 1
        else:
            res += curr
    return res

def binarySearch(lst, target, indexed):
    if target < lst[0][indexed]:
        return -1
    left, right = 0, len(lst) - 1
    while left < right and lst[right][indexed] > target:
        mid = left + (right - left) // 2
        if lst[mid][indexed] == target:
            return mid
        elif lst[mid][indexed] > target:
            right = mid - 1
        elif lst[mid][indexed] < target:
            left = mid + 1
    return right
def binarySearch2(lst, target):
    if target < lst[0]:
        return 0
    left, right = 0, len(lst) - 1
    while left < right and lst[right] > target:
        mid = left + (right - left) // 2
        if lst[mid] == target:
            return mid + 1
        elif lst[mid] > target:
            right = mid - 1
        elif lst[mid] < target:
            left = mid + 1
    return right + 1

lst = [(1, 20), (2, 19), (3, 18), (4, 17), (6, 16), (7, 15), (8, 14), (9, 13), (10, 12), (11, 11)]
# print(binarySearch(lst, 5, 0))
lst2 = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(binarySearch2(lst2, 1))
print(fancyPairPair(lst, 8, 36))
