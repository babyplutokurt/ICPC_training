Turn = int(input())
for i in range(Turn):
    length = int(input())
    lst = [int(j) for j in input().split()]

    if sum(lst) == 0:
        print(0)
    else:
        left, right = 0, 0
        for i in range(length):
            if lst[i]:
                left = i
                break
        for j in range(left, length - 1):
            if lst[j] and lst[j + 1] == 0:
                right = j
        if lst[-1]:
            right = length - 1

        if 0 in lst[left: right + 1]:
            print(2)
        else:
            print(1)