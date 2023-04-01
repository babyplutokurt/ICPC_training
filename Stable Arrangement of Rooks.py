turn = int(input())
for t in range(turn):
    lst = [int(i) for i in input().split()]
    b = lst[0]
    n = lst[1]
    if n > (b + 1) / 2:
        print(-1)
    else:
        index = 0
        R_count = 0
        for i in range(b):
            temp = []
            if R_count < n and i % 2 == 0:
                temp = "." * (index - 0) + "R" + "." * (b - index - 1)
                R_count += 1
                index += 2
            else:
                temp = "." * b
            print(temp)

