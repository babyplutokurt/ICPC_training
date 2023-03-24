Turn = int(input())
for i in range(Turn):
    lst = [int(i) for i in input().split()]
    if (lst[1] > lst[0] > lst[2]) or (lst[1] < lst[0] < lst[2]):
        print(lst[0])
    elif (lst[0] > lst[1] > lst[2]) or (lst[0] < lst[1] < lst[2]):
        print(lst[1])
    else:
        print(lst[2])