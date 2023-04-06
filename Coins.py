turn = int(input())
for t in range(turn):
    lst = [int(i) for i in input().split()]
    k = lst[1]
    n = lst[0]

    if k % 2 == 0 and n % 2 == 0:
        print("YES")
    elif k % 2 == 0 and n % 2 == 1:
        print("NO")
    elif k % 2 == 1:
        if n % 2 == 1:
            print("YES")
        elif n % 2 == 0:
            if n >= k * 2:
                print("YES")
            else:
                print("YES")
