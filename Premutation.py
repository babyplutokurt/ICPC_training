turn = int(input())
for t in range(turn):
    nums = int(input())

    lst = []
    for i in range(nums):
        lst.append([int(i) for i in input().split()])
    if nums <= 1:
        print(lst[0][0])
    elif nums == 3:
        mid = str(lst[0][-1]) + str(lst[1][-1]) + str(lst[2][-1])
        for i in range(1, 4, 1):
            if mid.count(str(i)) == 1:
                mid = str(i)
        for l in lst:
            if int(mid) not in l:
                print(str(l[0]) + " " + mid + ' ' + str(l[1]))
    else:
        test = lst[0]
        index = -1
        for i in range(1, nums):
            if lst[0][1:] == lst[i][:-1]:
                s = ''
                for num in (lst[0] + [lst[i][-1]]):
                    s += str(num) + ' '

            elif lst[0][:-1] == lst[i][1:]:
                s = ''
                for num in (lst[i] + [lst[0][-1]]):
                    s += str(num) + ' '
        print(s[:-1])