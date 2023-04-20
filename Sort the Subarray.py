for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(j) for j in input().split()]
    left, right = 0, 0
    for i in range(n):
        if a[i] != b[i]:
            left = i
            break
    for j in range(left, n):
        if a[j] == b[j]:
            right = j - 1
            break
    if right < left:
        right = n - 1

    for i in range(left, 0, -1):
        if b[i] >= b[i - 1]:
            left -= 1
        else:
            break

    for j in range(right, n - 1, 1):
        if b[j + 1] >= b[j]:
            right += 1
        else:
            break
    print(str(left + 1) + ' ' + str(right + 1))


