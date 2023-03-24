turns = int(input())
for turn in range(turns):
    lst1 = [int(i) for i in input().split()]
    nums = [int(j) for j in input().split()]
    n = lst1[0]
    k = lst1[1]
    index = 0
    pointer = 1

    for num in nums:
        if num == pointer:
            index += 1
            pointer += 1

    if (n - index) % k == 0:
        print((n - index) // k)
    else:
        print((n - index) // k + 1)
