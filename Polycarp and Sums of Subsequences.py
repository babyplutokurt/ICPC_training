turn = int(input())
for t in range(turn):
    lst = [int(i) for i in input().split()]
    total = lst[-1]
    s1 = total - lst[-2]
    s2 = total - lst[-3]
    lst = lst[0:4]
    s1s2 = s1 + s2
    lst.remove(s1)
    lst.remove(s2)
    lst.remove(s1s2)
    s3 = lst[0]
    print(s1, s2, s3)