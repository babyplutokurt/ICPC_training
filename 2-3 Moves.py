Turn = int(input())
for i in range(Turn):
    target = int(input())
    if target == 1:
        print(2)
    elif target % 3 == 0:
        print(target // 3)
    elif (target + 1) % 3 == 0:
        print((target + 1) // 3)
    else:
        print((target + 2) // 3)