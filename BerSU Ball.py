girl = int(input())
girls = [int(i) for i in input().split()]
boy = int(input())
boys = [int(i) for i in input().split()]

if girl > boy:
    girl, boy = boy, girl
    girls, boys = boys, girls
girls.sort()
boys.sort()
start = 0
res = 0
for p in range(girl):
    for b in range(start, boy):
        if abs(girls[p] - boys[b]) <= 1 :
            res += 1
            start = b + 1
            break
print(res)

