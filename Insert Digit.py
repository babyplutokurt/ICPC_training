turn = int(input())
for t in range(turn):
    lst = [i for i in input().split()]
    num = input()
    insert = False
    for c in range(len(num)):
        if num[c] < lst[1]:
            num = num[0:c] + lst[1] + num[c:]
            insert = True
            break
    if not insert:
        num = num + lst[1]
    print(num)