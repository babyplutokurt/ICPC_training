Turn = int(input())


def checkList(lst):
    ele = lst[0]
    chk = True

    for item in lst:
        if ele != item:
            chk = False
            break
    return chk


for i in range(Turn):
    length = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    lst = []
    max_0 = 0
    for j in range(length):
        if B[j]:
            lst.append(A[j] - B[j])
        else:
            max_0 = max(A[j] - B[j], max_0)
    if not lst:
        print("YES")
    elif checkList(lst) and max_0 <= lst[0]:
        print("YES")
    else:
        print("NO")
